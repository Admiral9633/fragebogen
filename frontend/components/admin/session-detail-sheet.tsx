"use client";

import { useEffect, useState } from "react";
import {
  AlertTriangle,
  CheckCircle2,
  Clock,
  Download,
  Info,
  Link2,
  Mail,
  OctagonAlert,
  Send,
} from "lucide-react";

import { cn } from "@/lib/utils";
import {
  answerDisplay,
  isVisible,
  isV2Schema,
  type EvaluationFinding,
  type EvaluationResult,
  type Question,
  type Schema,
  type Schwere,
} from "@/lib/schema";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import { Skeleton } from "@/components/ui/skeleton";
import { Spinner } from "@/components/ui/spinner";

export interface SessionDetail {
  token: string;
  patient_last_name: string;
  patient_first_name: string;
  patient_email: string;
  patient_birth_date: string;
  completed: boolean;
  completed_at: string | null;
  created_at: string;
  expires_at: string;
  expired: boolean;
  invitation_sent_at: string | null;
  gdt_patient_id: string;
  gdt_request_id: string;
  gdt_result_delivered_at: string | null;
  answers: Record<string, unknown> | null;
  schema: unknown;
  evaluation: EvaluationResult | null;
  ess_total: number | null;
  ess_band: string | null;
}

const SCHWERE_META: Record<
  Schwere,
  { label: string; icon: typeof Info; card: string; badge: string }
> = {
  kritisch: {
    label: "KRITISCH",
    icon: OctagonAlert,
    card: "border-destructive/40 bg-destructive/5",
    badge: "bg-destructive text-white",
  },
  pruefen: {
    label: "PRÜFEN",
    icon: AlertTriangle,
    card: "border-warning/50 bg-warning/10",
    badge: "bg-warning text-warning-foreground",
  },
  hinweis: {
    label: "HINWEIS",
    icon: Info,
    card: "border-border bg-muted/40",
    badge: "bg-muted text-muted-foreground",
  },
};

function FindingCard({ finding }: { finding: EvaluationFinding }) {
  const meta = SCHWERE_META[finding.schwere];
  const Icon = meta.icon;
  return (
    <div className={cn("rounded-lg border p-3", meta.card)}>
      <div className="flex items-start gap-2">
        <Icon
          className={cn(
            "mt-0.5 size-4 shrink-0",
            finding.schwere === "kritisch"
              ? "text-destructive"
              : finding.schwere === "pruefen"
                ? "text-warning"
                : "text-muted-foreground"
          )}
        />
        <div className="min-w-0 flex-1 space-y-1">
          <div className="flex flex-wrap items-center gap-2">
            <span className={cn("rounded px-1.5 py-0.5 text-[10px] font-black tracking-wide", meta.badge)}>
              {meta.label}
            </span>
            <span className="text-sm font-semibold">{finding.bereich}</span>
            <span className="text-xs text-muted-foreground">Kap. {finding.kapitel}</span>
          </div>
          <p className="text-sm text-foreground/90">{finding.befund}</p>
          <p className="text-sm font-medium text-foreground">
            <span className="text-muted-foreground">Vorgehen: </span>
            {finding.konsequenz}
          </p>
        </div>
      </div>
    </div>
  );
}

function AnswerRows({
  schema,
  answers,
}: {
  schema: Schema;
  answers: Record<string, unknown>;
}) {
  return (
    <div className="space-y-4">
      {schema.sections.map((section, i) => {
        const visible = section.questions.filter((q) => isVisible(q, answers));
        const rows = visible.flatMap((q: Question) => {
          if (q.type === "ess_matrix") return [];
          const value = answers[q.id];
          if (value === undefined || value === null || value === "") return [];
          const auffaellig = q.type === "yes_no" && value === "yes";
          const follow =
            q.followup && answers[q.followup.id]
              ? String(answers[q.followup.id])
              : null;
          return [
            <div
              key={q.id}
              className={cn(
                "flex items-baseline justify-between gap-3 border-l-2 py-1 pl-2 text-sm",
                auffaellig
                  ? "border-warning bg-warning/10 font-medium"
                  : "border-transparent"
              )}
            >
              <span className="min-w-0 flex-1 text-foreground/80">{q.label}</span>
              <span className={cn("shrink-0 font-semibold", auffaellig && "text-warning")}>
                {answerDisplay(q, value)}
              </span>
              {follow && (
                <span className="w-full basis-full pl-1 text-xs italic text-muted-foreground">
                  {follow}
                </span>
              )}
            </div>,
          ];
        });
        if (rows.length === 0) return null;
        return (
          <div key={section.id}>
            <h4 className="mb-1 text-xs font-bold uppercase tracking-wide text-muted-foreground">
              {i + 1}. {section.title}
            </h4>
            <div className="space-y-0.5">{rows}</div>
          </div>
        );
      })}
    </div>
  );
}

interface SessionDetailSheetProps {
  token: string | null;
  headers: Record<string, string>;
  onClose: () => void;
  onResend: (token: string) => void;
  onCopyLink: (token: string) => void;
}

export function SessionDetailSheet({
  token,
  headers,
  onClose,
  onResend,
  onCopyLink,
}: SessionDetailSheetProps) {
  const [detail, setDetail] = useState<SessionDetail | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!token) {
      setDetail(null);
      return;
    }
    let cancelled = false;
    setLoading(true);
    (async () => {
      try {
        const res = await fetch(`/api/admin/sessions/${token}/detail/`, { headers });
        if (!cancelled && res.ok) setDetail(await res.json());
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  const name = detail
    ? `${detail.patient_last_name}, ${detail.patient_first_name}`.replace(/^, |, $/, "") ||
      "Unbenannt"
    : "";
  const schema = detail && isV2Schema(detail.schema) ? detail.schema : null;
  const z = detail?.evaluation?.zusammenfassung;

  return (
    <Sheet open={!!token} onOpenChange={(open) => !open && onClose()}>
      <SheetContent side="right" className="w-full overflow-y-auto sm:max-w-xl">
        {loading || !detail ? (
          <div className="space-y-3 p-6">
            <Skeleton className="h-6 w-2/3" />
            <Skeleton className="h-24 w-full" />
            <Skeleton className="h-40 w-full" />
          </div>
        ) : (
          <>
            <SheetHeader className="pb-2">
              <SheetTitle className="flex flex-wrap items-center gap-2">
                {name}
                {detail.completed ? (
                  <Badge variant="success" className="gap-1">
                    <CheckCircle2 className="size-3" /> Ausgefüllt
                  </Badge>
                ) : detail.expired ? (
                  <Badge variant="destructive">Abgelaufen</Badge>
                ) : (
                  <Badge variant="warning" className="gap-1">
                    <Clock className="size-3" /> Offen
                  </Badge>
                )}
              </SheetTitle>
              <SheetDescription>
                {detail.patient_birth_date && <>Geb. {detail.patient_birth_date} · </>}
                Erstellt {detail.created_at} · Gültig bis {detail.expires_at}
              </SheetDescription>
            </SheetHeader>

            <div className="space-y-5 px-4 pb-8">
              {/* Status / GDT */}
              <div className="grid grid-cols-2 gap-2 text-sm">
                <div className="rounded-lg border p-2.5">
                  <p className="text-xs text-muted-foreground">Einladung</p>
                  <p className="font-medium">
                    {detail.invitation_sent_at
                      ? `versendet ${detail.invitation_sent_at}`
                      : detail.patient_email
                        ? "noch nicht versendet"
                        : "keine E-Mail hinterlegt"}
                  </p>
                </div>
                <div className="rounded-lg border p-2.5">
                  <p className="text-xs text-muted-foreground">SAMAS / GDT</p>
                  {detail.gdt_patient_id ? (
                    <p className="font-medium">
                      ID {detail.gdt_patient_id}
                      {detail.gdt_result_delivered_at ? (
                        <span className="block text-xs text-success">
                          ✓ Ergebnis übermittelt {detail.gdt_result_delivered_at}
                        </span>
                      ) : detail.completed ? (
                        <span className="block text-xs text-warning">
                          wartet auf Abholung durch die Bridge
                        </span>
                      ) : (
                        <span className="block text-xs text-muted-foreground">
                          Link-GDT an SAMAS geschrieben – Praxisbetrieb läuft weiter
                        </span>
                      )}
                    </p>
                  ) : (
                    <p className="text-muted-foreground">ohne GDT angelegt</p>
                  )}
                </div>
              </div>

              {/* Aktionen */}
              <div className="flex flex-wrap gap-2">
                <Button size="sm" variant="outline" onClick={() => onCopyLink(detail.token)}>
                  <Link2 className="size-4" /> Link kopieren
                </Button>
                {detail.completed && (
                  <Button size="sm" asChild>
                    <a
                      href={`/api/puppeteer-pdf/${detail.token}`}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <Download className="size-4" /> PDF öffnen
                    </a>
                  </Button>
                )}
                {!detail.completed && detail.patient_email && (
                  <Button size="sm" variant="outline" onClick={() => onResend(detail.token)}>
                    <Mail className="size-4" /> Einladung erneut senden
                  </Button>
                )}
              </div>

              {/* Auswertung */}
              {detail.completed && detail.evaluation && (
                <div>
                  <Separator className="mb-4" />
                  <div className="mb-3 flex flex-wrap items-center gap-2">
                    <h3 className="text-sm font-bold uppercase tracking-wide">
                      Automatische Auswertung
                    </h3>
                    <Badge variant="outline">
                      Gruppe {detail.evaluation.gruppe2 ? "2" : "1"}
                    </Badge>
                    {detail.ess_total !== null && (
                      <Badge
                        variant={
                          (detail.ess_total ?? 0) >= 16
                            ? "destructive"
                            : (detail.ess_total ?? 0) >= 11
                              ? "warning"
                              : "success"
                        }
                      >
                        ESS {detail.ess_total}/24
                      </Badge>
                    )}
                  </div>
                  {z && z.kritisch === 0 && z.pruefen === 0 && z.hinweis === 0 ? (
                    <div className="rounded-lg border border-success/40 bg-success/10 p-3 text-sm font-medium text-success">
                      Keine eignungsrelevanten Auffälligkeiten aus den Angaben ableitbar.
                    </div>
                  ) : (
                    <div className="space-y-2">
                      {detail.evaluation.findings.map((f, i) => (
                        <FindingCard key={i} finding={f} />
                      ))}
                    </div>
                  )}
                  <p className="mt-2 text-xs italic text-muted-foreground">
                    {detail.evaluation.disclaimer}
                  </p>
                </div>
              )}

              {/* Antworten */}
              {detail.completed && detail.answers && schema && (
                <div>
                  <Separator className="mb-4" />
                  <h3 className="mb-3 text-sm font-bold uppercase tracking-wide">
                    Antworten
                    <span className="ml-2 font-normal normal-case text-muted-foreground">
                      (auffällige Ja-Antworten hervorgehoben)
                    </span>
                  </h3>
                  <AnswerRows schema={schema} answers={detail.answers} />
                </div>
              )}

              {!detail.completed && (
                <div className="rounded-lg border border-dashed p-4 text-center text-sm text-muted-foreground">
                  <Send className="mx-auto mb-2 size-5" />
                  Der Fragebogen wurde noch nicht ausgefüllt.
                </div>
              )}
            </div>
          </>
        )}
        {loading && detail && (
          <div className="absolute right-4 top-4">
            <Spinner className="size-4" />
          </div>
        )}
      </SheetContent>
    </Sheet>
  );
}
