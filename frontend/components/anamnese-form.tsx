"use client";

import { useMemo, useState } from "react";

import { cn } from "@/lib/utils";
import { calcESS } from "@/lib/ess";
import { UI_DE, type UiStrings } from "@/lib/i18n";
import {
  isVisible,
  type Answers,
  type Question,
  type Schema,
} from "@/lib/schema";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Questionnaire,
  QuestionnaireActions,
  QuestionnaireChoice,
  QuestionnaireChoices,
  QuestionnaireDescription,
  QuestionnaireError,
  QuestionnaireInput,
  QuestionnaireItem,
  QuestionnaireNext,
  QuestionnairePrevious,
  QuestionnaireProgress,
  QuestionnaireSkip,
  QuestionnaireSubmit,
  QuestionnaireTitle,
} from "@/components/ui/questionnaire";
import { Spinner } from "@/components/ui/spinner";

interface AnamneseFormProps {
  schema: Schema;
  onSubmit: (data: Record<string, unknown>) => Promise<void>;
  isSubmitting: boolean;
  /** Übersetzte UI-Texte (Default: Deutsch) */
  ui?: UiStrings;
}

// ─── Schema → flache Item-Liste (eine Frage pro Schritt) ─────────────────────

type ItemKind = "choice" | "multiple" | "input" | "ess" | "consent" | "followup";

interface FlatItem {
  name: string;
  kind: ItemKind;
  sectionIndex: number;
  sectionTitle: string;
  title: string;
  hint?: string;
  required: boolean;
  options?: { value: string; label: string }[];
  /** followup: Elternfrage + Auslösewert */
  parent?: { id: string; when: string };
  /** show_if der Original-Frage (für disabled) */
  question?: Question;
  essIndex?: number;
  consentError?: string;
}

function flattenSchema(schema: Schema, ui: UiStrings): FlatItem[] {
  const flat: FlatItem[] = [];
  const essOptions = [
    { value: "0", label: ui.ess_opt_0 },
    { value: "1", label: ui.ess_opt_1 },
    { value: "2", label: ui.ess_opt_2 },
    { value: "3", label: ui.ess_opt_3 },
  ];

  schema.sections.forEach((section, sectionIndex) => {
    for (const q of section.questions) {
      const base = {
        sectionIndex,
        sectionTitle: section.title,
        question: q,
      };

      if (q.type === "ess_matrix") {
        (q.items ?? []).forEach((essItem, i) => {
          flat.push({
            ...base,
            name: essItem.id,
            kind: "ess",
            title: `${essItem.label}`,
            hint: q.hint,
            required: q.required !== false,
            options: essOptions,
            essIndex: i + 1,
          });
        });
        continue;
      }

      if (q.type === "consent") {
        flat.push({
          ...base,
          name: q.id,
          kind: "consent",
          title: ui.consent_title,
          required: true,
          consentError: q.error,
        });
        continue;
      }

      if (q.type === "yes_no" || q.type === "choice") {
        flat.push({
          ...base,
          name: q.id,
          kind: "choice",
          title: q.label,
          hint: q.hint,
          required: q.required !== false,
          options:
            q.type === "yes_no"
              ? [
                  { value: "yes", label: ui.yes },
                  { value: "no", label: ui.no },
                ]
              : (q.options ?? []),
        });
      } else if (q.type === "multi_choice") {
        flat.push({
          ...base,
          name: q.id,
          kind: "multiple",
          title: q.label,
          hint: q.hint,
          required: q.required !== false,
          options: q.options ?? [],
        });
      } else if (q.type === "text" || q.type === "textarea") {
        flat.push({
          ...base,
          name: q.id,
          kind: "input",
          title: q.label,
          hint: q.hint,
          required: q.required !== false,
        });
      }

      if (q.followup) {
        flat.push({
          ...base,
          name: q.followup.id,
          kind: "followup",
          title: q.followup.label,
          required: false,
          parent: { id: q.id, when: q.followup.when ?? "yes" },
        });
      }
    }
  });

  return flat;
}

function isItemEnabled(item: FlatItem, answers: Answers): boolean {
  if (item.parent) {
    return answers[item.parent.id] === item.parent.when;
  }
  if (item.question && !isVisible(item.question, answers)) {
    return false;
  }
  return true;
}

/** Nur beantwortete, aktuell aktive Fragen einsammeln; ESS-Werte als int. */
function collectPayload(flat: FlatItem[], answers: Answers): Record<string, unknown> {
  const payload: Record<string, unknown> = {};
  for (const item of flat) {
    if (!isItemEnabled(item, answers)) continue;
    const v = answers[item.name];
    if (v === undefined || v === null || v === "") continue;
    if (item.kind === "ess") {
      payload[item.name] = parseInt(String(v), 10);
    } else if (item.kind === "consent") {
      if (v === true) payload[item.name] = true;
    } else if (item.kind === "multiple") {
      if (Array.isArray(v) && v.length > 0) payload[item.name] = v;
    } else if (typeof v === "string" && v.trim() !== "") {
      payload[item.name] = v.trim();
    }
  }
  return payload;
}

// ─── Datenschutz-Dialog ───────────────────────────────────────────────────────

function PrivacyDialog({
  open,
  onOpenChange,
  ui,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  ui: UiStrings;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-h-[85vh] overflow-y-auto sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>{ui.privacy_title}</DialogTitle>
          <DialogDescription>{ui.privacy_subtitle}</DialogDescription>
        </DialogHeader>
        <div className="space-y-3 text-sm text-foreground/90">
          <p>{ui.privacy_controller}</p>
          <p>{ui.privacy_purpose}</p>
          <p>{ui.privacy_legal}</p>
          <p>{ui.privacy_storage}</p>
          <p>{ui.privacy_rights}</p>
          <p>{ui.privacy_secrecy}</p>
        </div>
      </DialogContent>
    </Dialog>
  );
}

// ─── Haupt-Komponente ─────────────────────────────────────────────────────────

export function AnamneseForm({ schema, onSubmit, isSubmitting, ui = UI_DE }: AnamneseFormProps) {
  const flat = useMemo(() => flattenSchema(schema, ui), [schema, ui]);
  const [answers, setAnswers] = useState<Answers>({});
  const [showPrivacy, setShowPrivacy] = useState(false);

  const setAnswer = (name: string, value: unknown) =>
    setAnswers((prev) => ({ ...prev, [name]: value }));

  const toggleMulti = (name: string, value: string) =>
    setAnswers((prev) => {
      const cur = Array.isArray(prev[name]) ? (prev[name] as string[]) : [];
      return {
        ...prev,
        [name]: cur.includes(value) ? cur.filter((v) => v !== value) : [...cur, value],
      };
    });

  // Item-Definitionen (Reihenfolge + disabled) für das Questionnaire-Primitive
  const itemDefs = useMemo(
    () =>
      flat.map((item) => {
        const enabled = isItemEnabled(item, answers);
        return {
          name: item.name,
          required: enabled && item.required,
          disabled: !enabled,
        };
      }),
    [flat, answers]
  );

  // Aktive Items in Anzeige-Reihenfolge (für Sektionsanzeige im Progress)
  const enabledFlat = useMemo(
    () => flat.filter((item) => isItemEnabled(item, answers)),
    [flat, answers]
  );

  const sectionCount = schema.sections.length;
  const { total: essTotal } = calcESS(answers);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (isSubmitting) return;
    await onSubmit(collectPayload(flat, answers));
  };

  return (
    <>
      <Questionnaire
        items={itemDefs}
        shortcuts="numbers"
        onSubmit={handleSubmit}
        className="gap-6"
      >
        {/* Fortschritt: Sektions-Segmente + Frage-Zähler */}
        <QuestionnaireProgress
          className="w-full"
          render={(props, state) => {
            const current = enabledFlat[state.current - 1];
            const sectionIndex = current?.sectionIndex ?? 0;
            return (
              <div {...props}>
                <div className="mb-2 flex gap-1" aria-hidden="true">
                  {Array.from({ length: sectionCount }, (_, i) => (
                    <span
                      key={i}
                      className={cn(
                        "h-1.5 flex-1 rounded-full transition-colors",
                        i < sectionIndex
                          ? "bg-primary"
                          : i === sectionIndex
                            ? "bg-primary/50"
                            : "bg-muted"
                      )}
                    />
                  ))}
                </div>
                <div className="flex items-baseline justify-between gap-2">
                  <span className="text-sm font-semibold text-foreground">
                    {current?.sectionTitle}
                  </span>
                  <span className="text-xs tabular-nums text-muted-foreground">
                    {ui.question_of
                      .replace("{current}", String(state.current))
                      .replace("{total}", String(state.total))}
                  </span>
                </div>
              </div>
            );
          }}
        />

        {flat.map((item) => (
          <QuestionnaireItem
            key={item.name}
            name={item.name}
            required={item.required}
            multiple={item.kind === "multiple" || item.kind === "consent"}
            disabled={!isItemEnabled(item, answers)}
          >
            <QuestionnaireTitle>
              {item.kind === "ess" ? `${item.essIndex}. ${item.title}` : item.title}
            </QuestionnaireTitle>

            {item.kind === "ess" && (
              <QuestionnaireDescription>
                {ui.ess_question} · {ui.ess_sum}: {essTotal}/24
              </QuestionnaireDescription>
            )}
            {item.kind !== "ess" && item.hint && (
              <QuestionnaireDescription>{item.hint}</QuestionnaireDescription>
            )}
            {item.kind === "followup" && (
              <QuestionnaireDescription>{ui.followup_hint}</QuestionnaireDescription>
            )}
            {item.kind === "consent" && item.name === "consent_privacy" && (
              <QuestionnaireDescription
                render={
                  <div className="text-sm text-muted-foreground">
                    <button
                      type="button"
                      className="font-semibold text-primary underline underline-offset-2"
                      onClick={() => setShowPrivacy(true)}
                    >
                      {ui.privacy_button}
                    </button>
                  </div>
                }
              />
            )}

            {item.kind === "input" || item.kind === "followup" ? (
              <QuestionnaireChoices>
                <QuestionnaireInput
                  aria-label={item.title}
                  value={(answers[item.name] as string) ?? ""}
                  onChange={(e) => setAnswer(item.name, e.target.value)}
                  placeholder={ui.answer_placeholder}
                />
              </QuestionnaireChoices>
            ) : item.kind === "consent" ? (
              <QuestionnaireChoices>
                <QuestionnaireChoice
                  value="ja"
                  checked={answers[item.name] === true}
                  onChange={(e) => setAnswer(item.name, e.target.checked)}
                >
                  <span className="font-medium">{item.question?.label}</span>
                </QuestionnaireChoice>
              </QuestionnaireChoices>
            ) : (
              <QuestionnaireChoices>
                {(item.options ?? []).map((opt) =>
                  item.kind === "multiple" ? (
                    <QuestionnaireChoice
                      key={opt.value}
                      value={opt.value}
                      checked={
                        Array.isArray(answers[item.name]) &&
                        (answers[item.name] as string[]).includes(opt.value)
                      }
                      onChange={() => toggleMulti(item.name, opt.value)}
                    >
                      {opt.label}
                    </QuestionnaireChoice>
                  ) : (
                    <QuestionnaireChoice
                      key={opt.value}
                      value={opt.value}
                      checked={answers[item.name] === opt.value}
                      onChange={() => setAnswer(item.name, opt.value)}
                    >
                      {opt.label}
                    </QuestionnaireChoice>
                  )
                )}
              </QuestionnaireChoices>
            )}

            <QuestionnaireError>
              {item.consentError ?? ui.required_error}
            </QuestionnaireError>
          </QuestionnaireItem>
        ))}

        <QuestionnaireActions>
          <QuestionnairePrevious>{ui.back}</QuestionnairePrevious>
          <QuestionnaireSkip>{ui.skip}</QuestionnaireSkip>
          <QuestionnaireNext>{ui.next}</QuestionnaireNext>
          <QuestionnaireSubmit disabled={isSubmitting}>
            {isSubmitting ? (
              <>
                <Spinner /> {ui.sending}
              </>
            ) : (
              ui.submit
            )}
          </QuestionnaireSubmit>
        </QuestionnaireActions>
      </Questionnaire>

      <PrivacyDialog open={showPrivacy} onOpenChange={setShowPrivacy} ui={ui} />
    </>
  );
}
