"use client";

import { useEffect, useRef, useState } from "react";
import { Control, Controller, FieldErrors, useForm } from "react-hook-form";
import { ChevronLeft, ChevronRight } from "lucide-react";

import { cn } from "@/lib/utils";
import { calcESS } from "@/lib/ess";
import {
  Answers,
  Question,
  Schema,
  Section,
  visibleQuestions,
} from "@/lib/schema";
import { Button } from "@/components/ui/button";
import { ButtonGroup } from "@/components/ui/button-group";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSet,
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Spinner } from "@/components/ui/spinner";
import { Textarea } from "@/components/ui/textarea";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

const REQUIRED_MSG = "Bitte beantworten Sie diese Frage.";

type FormValues = Record<string, unknown>;

interface AnamneseFormProps {
  schema: Schema;
  onSubmit: (data: Record<string, unknown>) => Promise<void>;
  isSubmitting: boolean;
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

/** Feldnamen einer Fragenliste (inkl. ESS-Items und aktiver Followups). */
function fieldNames(questions: Question[], values: Answers): string[] {
  const names: string[] = [];
  for (const q of questions) {
    if (q.type === "ess_matrix") {
      names.push(...(q.items ?? []).map((item) => item.id));
      continue;
    }
    names.push(q.id);
    if (q.followup && values[q.id] === (q.followup.when ?? "yes")) {
      names.push(q.followup.id);
    }
  }
  return names;
}

/** Nur beantwortete, aktuell sichtbare Felder einsammeln; ESS-Werte als int. */
function collectPayload(schema: Schema, values: FormValues): Record<string, unknown> {
  const payload: Record<string, unknown> = {};
  for (const section of schema.sections) {
    for (const q of visibleQuestions(section, values)) {
      if (q.type === "ess_matrix") {
        for (const item of q.items ?? []) {
          const v = values[item.id];
          if (typeof v === "string" && v !== "") payload[item.id] = parseInt(v, 10);
        }
        continue;
      }
      const v = values[q.id];
      if (q.type === "consent") {
        if (v === true) payload[q.id] = true;
      } else if (q.type === "multi_choice") {
        if (Array.isArray(v) && v.length > 0) payload[q.id] = v;
      } else if (typeof v === "string" && v.trim() !== "") {
        payload[q.id] = v;
      }
      const f = q.followup;
      if (f && values[q.id] === (f.when ?? "yes")) {
        const fv = values[f.id];
        if (typeof fv === "string" && fv.trim() !== "") payload[f.id] = fv;
      }
    }
  }
  return payload;
}

// ─── Frage-Renderer ───────────────────────────────────────────────────────────

interface QuestionProps {
  question: Question;
  control: Control<FormValues>;
  values: Answers;
  onOpenPrivacy: () => void;
}

function RadioQuestion({
  question,
  control,
  options,
  horizontal,
}: {
  question: Question;
  control: Control<FormValues>;
  options: { value: string; label: string }[];
  horizontal: boolean;
}) {
  return (
    <Controller
      name={question.id}
      control={control}
      rules={{ required: question.required ? REQUIRED_MSG : false }}
      render={({ field, fieldState }) => (
        <FieldSet data-invalid={fieldState.invalid}>
          <FieldLegend variant="label">{question.label}</FieldLegend>
          {question.hint && <FieldDescription>{question.hint}</FieldDescription>}
          <RadioGroup
            name={field.name}
            value={(field.value as string) ?? ""}
            onValueChange={field.onChange}
            aria-invalid={fieldState.invalid}
            className={cn(horizontal && "flex flex-row flex-wrap gap-6")}
          >
            {options.map((opt) => (
              <Field
                key={opt.value}
                orientation="horizontal"
                data-invalid={fieldState.invalid}
                className="w-fit"
              >
                <RadioGroupItem
                  value={opt.value}
                  id={`${question.id}-${opt.value}`}
                  aria-invalid={fieldState.invalid}
                />
                <FieldLabel
                  htmlFor={`${question.id}-${opt.value}`}
                  className="font-normal"
                >
                  {opt.label}
                </FieldLabel>
              </Field>
            ))}
          </RadioGroup>
          {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
        </FieldSet>
      )}
    />
  );
}

function MultiChoiceQuestion({ question, control }: QuestionProps) {
  return (
    <Controller
      name={question.id}
      control={control}
      rules={{
        validate: (v) =>
          !question.required || (Array.isArray(v) && v.length > 0) || REQUIRED_MSG,
      }}
      render={({ field, fieldState }) => (
        <FieldSet data-invalid={fieldState.invalid}>
          <FieldLegend variant="label">{question.label}</FieldLegend>
          {question.hint && <FieldDescription>{question.hint}</FieldDescription>}
          <ToggleGroup
            type="multiple"
            variant="outline"
            spacing={2}
            value={(field.value as string[]) ?? []}
            onValueChange={field.onChange}
            aria-invalid={fieldState.invalid}
            className="flex-wrap justify-start"
          >
            {(question.options ?? []).map((opt) => (
              <ToggleGroupItem key={opt.value} value={opt.value} aria-label={opt.label}>
                {opt.label}
              </ToggleGroupItem>
            ))}
          </ToggleGroup>
          {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
        </FieldSet>
      )}
    />
  );
}

function TextQuestion({ question, control }: QuestionProps) {
  const isTextarea = question.type === "textarea";
  return (
    <Controller
      name={question.id}
      control={control}
      rules={{ required: question.required ? REQUIRED_MSG : false }}
      render={({ field, fieldState }) => (
        <Field data-invalid={fieldState.invalid}>
          <FieldLabel htmlFor={question.id}>{question.label}</FieldLabel>
          {isTextarea ? (
            <Textarea
              {...field}
              value={(field.value as string) ?? ""}
              id={question.id}
              aria-invalid={fieldState.invalid}
            />
          ) : (
            <Input
              {...field}
              value={(field.value as string) ?? ""}
              id={question.id}
              aria-invalid={fieldState.invalid}
            />
          )}
          {question.hint && <FieldDescription>{question.hint}</FieldDescription>}
          {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
        </Field>
      )}
    />
  );
}

/** Eingerücktes Detailfeld unter der Elternfrage (optional, nie Pflicht). */
function FollowupField({ question, control, values }: QuestionProps) {
  const f = question.followup;
  if (!f || values[question.id] !== (f.when ?? "yes")) return null;
  const isTextarea = f.type !== "text";
  return (
    <div className="ml-2 border-l-2 border-primary/30 pl-4">
      <Controller
        name={f.id}
        control={control}
        render={({ field }) => (
          <Field>
            <FieldLabel htmlFor={f.id} className="font-normal">
              {f.label}
            </FieldLabel>
            {isTextarea ? (
              <Textarea
                {...field}
                value={(field.value as string) ?? ""}
                id={f.id}
                rows={3}
              />
            ) : (
              <Input {...field} value={(field.value as string) ?? ""} id={f.id} />
            )}
          </Field>
        )}
      />
    </div>
  );
}

const ESS_BAND_STYLES: Record<
  string,
  { box: string; text: string; badge: string }
> = {
  normal: {
    box: "border-success/50 bg-success/10",
    text: "text-success",
    badge: "bg-success text-success-foreground",
  },
  erhöht: {
    box: "border-warning/50 bg-warning/10",
    text: "text-warning",
    badge: "bg-warning text-warning-foreground",
  },
  ausgeprägt: {
    box: "border-destructive/50 bg-destructive/10",
    text: "text-destructive",
    badge: "bg-destructive text-destructive-foreground",
  },
};

function EssMatrixQuestion({ question, control, values }: QuestionProps) {
  const { total, band, bandLabel } = calcESS(values);
  const styles = ESS_BAND_STYLES[band] ?? ESS_BAND_STYLES.normal;

  return (
    <div className="space-y-5 rounded-xl border border-primary/25 bg-primary/5 p-4">
      <div>
        <p className="text-sm font-semibold">{question.label}</p>
        {question.hint && (
          <p className="mt-1 text-xs text-muted-foreground">{question.hint}</p>
        )}
      </div>

      {(question.items ?? []).map((item, i) => (
        <Controller
          key={item.id}
          name={item.id}
          control={control}
          rules={{ required: question.required ? REQUIRED_MSG : false }}
          render={({ field, fieldState }) => (
            <FieldSet data-invalid={fieldState.invalid}>
              <FieldLegend variant="label" className="mb-2 text-xs font-medium">
                {i + 1}. {item.label}
              </FieldLegend>
              <RadioGroup
                name={field.name}
                value={(field.value as string) ?? ""}
                onValueChange={field.onChange}
                aria-invalid={fieldState.invalid}
                className="flex flex-row flex-wrap gap-6"
              >
                {["0", "1", "2", "3"].map((n) => (
                  <Field
                    key={n}
                    orientation="horizontal"
                    data-invalid={fieldState.invalid}
                    className="w-fit"
                  >
                    <RadioGroupItem
                      value={n}
                      id={`${item.id}-${n}`}
                      aria-invalid={fieldState.invalid}
                    />
                    <FieldLabel htmlFor={`${item.id}-${n}`} className="font-normal">
                      {n}
                    </FieldLabel>
                  </Field>
                ))}
              </RadioGroup>
              {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
            </FieldSet>
          )}
        />
      ))}

      {/* Live-Score */}
      <div
        className={cn(
          "flex items-center justify-between rounded-xl border-2 p-4",
          styles.box
        )}
      >
        <div>
          <p className="text-2xl font-bold text-foreground">
            {total}{" "}
            <span className="text-base font-normal text-muted-foreground">
              / 24 Punkte
            </span>
          </p>
          <p className={cn("mt-0.5 text-sm font-semibold", styles.text)}>
            {bandLabel}
          </p>
        </div>
        <div
          className={cn(
            "flex size-14 items-center justify-center rounded-full text-xl font-black",
            styles.badge
          )}
        >
          {total}
        </div>
      </div>
    </div>
  );
}

function ConsentQuestion({ question, control, onOpenPrivacy }: QuestionProps) {
  const label = question.label;
  const marker = "Datenschutzhinweise";
  const idx = label.indexOf(marker);

  const labelContent =
    idx >= 0 ? (
      <span>
        {label.slice(0, idx)}
        <button
          type="button"
          className="font-semibold underline underline-offset-2 hover:text-primary"
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            onOpenPrivacy();
          }}
        >
          {marker}
        </button>
        {label.slice(idx + marker.length)}
      </span>
    ) : (
      label
    );

  return (
    <Controller
      name={question.id}
      control={control}
      rules={{
        validate: (v) =>
          v === true || question.error || "Bitte bestätigen Sie diese Erklärung.",
      }}
      render={({ field, fieldState }) => (
        <Field orientation="horizontal" data-invalid={fieldState.invalid}>
          <Checkbox
            id={question.id}
            name={field.name}
            checked={field.value === true}
            onCheckedChange={(v) => field.onChange(v === true)}
            aria-invalid={fieldState.invalid}
          />
          <FieldContent>
            <FieldLabel htmlFor={question.id} className="font-normal">
              {labelContent}
            </FieldLabel>
            {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
          </FieldContent>
        </Field>
      )}
    />
  );
}

function QuestionField(props: QuestionProps) {
  const { question, control } = props;
  switch (question.type) {
    case "yes_no":
      return (
        <>
          <RadioQuestion
            question={question}
            control={control}
            options={[
              { value: "yes", label: "Ja" },
              { value: "no", label: "Nein" },
            ]}
            horizontal
          />
          <FollowupField {...props} />
        </>
      );
    case "choice":
      return (
        <>
          <RadioQuestion
            question={question}
            control={control}
            options={question.options ?? []}
            horizontal={false}
          />
          <FollowupField {...props} />
        </>
      );
    case "multi_choice":
      return <MultiChoiceQuestion {...props} />;
    case "text":
    case "textarea":
      return (
        <>
          <TextQuestion {...props} />
          <FollowupField {...props} />
        </>
      );
    case "ess_matrix":
      return <EssMatrixQuestion {...props} />;
    case "consent":
      return <ConsentQuestion {...props} />;
    default:
      return null;
  }
}

// ─── Datenschutz-Dialog ───────────────────────────────────────────────────────

function PrivacyDialog({
  open,
  onOpenChange,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-h-[85vh] overflow-y-auto sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Datenschutzhinweise</DialogTitle>
          <DialogDescription>
            Information zur Verarbeitung Ihrer Daten nach Art. 13 DSGVO
          </DialogDescription>
        </DialogHeader>
        <div className="space-y-3 text-sm text-foreground/90">
          <p>
            <strong>Verantwortlicher:</strong> Dr. med. Björn Micka, Betriebsmedizin ·
            Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach
          </p>
          <p>
            <strong>Zweck der Verarbeitung:</strong> Ihre Angaben in diesem Fragebogen
            (einschließlich Gesundheitsdaten) werden ausschließlich zur Vorbereitung und
            Durchführung Ihrer verkehrsmedizinischen Untersuchung verwendet.
          </p>
          <p>
            <strong>Rechtsgrundlage:</strong> Ihre Einwilligung (Art. 6 Abs. 1 lit. a,
            Art. 9 Abs. 2 lit. a DSGVO). Sie können die Einwilligung jederzeit mit Wirkung
            für die Zukunft widerrufen.
          </p>
          <p>
            <strong>Speicherung:</strong> Das Ergebnis wird in Ihre Untersuchungsunterlagen
            übernommen und unterliegt den ärztlichen Aufbewahrungsfristen. Der Online-Zugang
            über Ihren persönlichen Link erlischt nach Ablauf der Gültigkeit; die Daten
            dieses Online-Fragebogens werden anschließend routinemäßig gelöscht.
          </p>
          <p>
            <strong>Ihre Rechte:</strong> Sie haben das Recht auf Auskunft, Berichtigung,
            Löschung und Einschränkung der Verarbeitung sowie ein Beschwerderecht bei der
            zuständigen Datenschutz-Aufsichtsbehörde.
          </p>
          <p>Alle Angaben unterliegen der ärztlichen Schweigepflicht.</p>
        </div>
      </DialogContent>
    </Dialog>
  );
}

// ─── Haupt-Komponente ─────────────────────────────────────────────────────────

export function AnamneseForm({ schema, onSubmit, isSubmitting }: AnamneseFormProps) {
  const sections: Section[] = schema.sections;
  const [step, setStep] = useState(0);
  const [showPrivacy, setShowPrivacy] = useState(false);
  const headingRef = useRef<HTMLHeadingElement>(null);

  const form = useForm<FormValues>({ mode: "onTouched" });
  const values = form.watch();
  const { errors } = form.formState;

  const section = sections[step];
  const visible = visibleQuestions(section, values);
  const stepFields = fieldNames(visible, values);
  const stepErrorCount = stepFields.filter(
    (name) => (errors as FieldErrors)[name]
  ).length;
  const isLast = step === sections.length - 1;

  // Fokus + Scroll beim Schrittwechsel
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
    headingRef.current?.focus();
  }, [step]);

  const goNext = async () => {
    const ok = await form.trigger(stepFields, { shouldFocus: true });
    if (!ok) return;
    if (isLast) {
      await onSubmit(collectPayload(schema, form.getValues()));
    } else {
      setStep((s) => s + 1);
    }
  };

  const goBack = () => {
    if (step > 0) setStep((s) => s - 1);
  };

  return (
    <form
      noValidate
      onSubmit={(e) => {
        e.preventDefault();
        if (!isSubmitting) void goNext();
      }}
      className="space-y-6"
    >
      {/* Fortschritt */}
      <div className="space-y-2">
        <Progress value={((step + 1) / sections.length) * 100} className="h-1.5" />
        <p className="text-right text-xs text-muted-foreground">
          Schritt {step + 1} von {sections.length}
        </p>
      </div>

      {/* Schritt-Überschrift */}
      <div>
        <h2
          ref={headingRef}
          tabIndex={-1}
          className="text-2xl font-bold text-foreground outline-none"
        >
          {section.title}
        </h2>
        {section.subtitle && (
          <p className="mt-1 text-sm text-muted-foreground">{section.subtitle}</p>
        )}
      </div>

      {/* Fehler-Summary */}
      {stepErrorCount > 0 && (
        <div
          role="alert"
          className="rounded-lg border border-destructive/40 bg-destructive/10 px-4 py-3"
        >
          <p className="text-sm font-medium text-destructive">
            {stepErrorCount === 1
              ? "1 Frage ist noch unbeantwortet."
              : `${stepErrorCount} Fragen sind noch unbeantwortet.`}{" "}
            Bitte prüfen Sie Ihre Angaben.
          </p>
        </div>
      )}

      {/* Fragen des aktuellen Schritts */}
      <FieldGroup>
        {visible.map((q) => (
          <QuestionField
            key={q.id}
            question={q}
            control={form.control}
            values={values}
            onOpenPrivacy={() => setShowPrivacy(true)}
          />
        ))}
      </FieldGroup>

      {/* Navigation */}
      <div className="flex justify-end pb-4 pt-2">
        <ButtonGroup>
          <Button
            type="button"
            variant="outline"
            onClick={goBack}
            disabled={step === 0 || isSubmitting}
          >
            <ChevronLeft /> Zurück
          </Button>
          <Button type="submit" disabled={isSubmitting} className="min-w-[120px]">
            {isSubmitting ? (
              <>
                <Spinner /> Senden…
              </>
            ) : isLast ? (
              "Absenden"
            ) : (
              <>
                Weiter <ChevronRight />
              </>
            )}
          </Button>
        </ButtonGroup>
      </div>

      <PrivacyDialog open={showPrivacy} onOpenChange={setShowPrivacy} />
    </form>
  );
}
