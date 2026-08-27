"use client";

import { useEffect, useMemo, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { toast } from "sonner";
import { CheckCircle2, AlertCircle, Download, Car, Stethoscope } from "lucide-react";
import { cn } from "@/lib/utils";
import { AnamneseForm } from "@/components/anamnese-form";
import { LanguageSelect } from "@/components/language-select";
import { COUNTRIES, RTL_LANGUAGES } from "@/lib/countries";
import {
  fetchTranslation,
  translateSchema,
  uiStrings,
  type Translation,
} from "@/lib/i18n";
import { isV2Schema } from "@/lib/schema";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { badgeVariants } from "@/components/ui/badge";
import { ModeToggle } from "@/components/mode-toggle";
import { Spinner } from "@/components/ui/spinner";

const API_URL = ""; // Requests go via Next.js proxy rewrites → backend:8000

// DRF-Fehlerobjekte ({"feld": ["Meldung"]} oder {"error": "..."}) menschenlesbar machen
function extractApiError(d: unknown): string {
  if (!d || typeof d !== "object") return "Fehler beim Absenden. Bitte versuchen Sie es erneut.";
  const obj = d as Record<string, unknown>;
  if (typeof obj.error === "string") return obj.error;
  const first = Object.values(obj).flat().find((v) => typeof v === "string");
  return typeof first === "string" ? first : "Fehler beim Absenden. Bitte prüfen Sie Ihre Angaben.";
}

export default function QuestionnairePage() {
  const params = useParams();
  const router = useRouter();
  const token = params.token as string;

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [sessionData, setSessionData] = useState<any>(null);
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [result, setResult] = useState<any>(null);

  // ── Sprache ────────────────────────────────────────────────────────────────
  const [country, setCountry] = useState("de");
  const [lang, setLang] = useState("de");
  const [translation, setTranslation] = useState<Translation | null>(null);
  const [availableLangs, setAvailableLangs] = useState<Set<string> | undefined>();

  useEffect(() => {
    (async () => {
      try {
        const res = await fetch("/api/i18n");
        if (res.ok) {
          const d = await res.json();
          if (Array.isArray(d.languages)) setAvailableLangs(new Set(d.languages));
        }
      } catch {
        // ohne Liste bleiben alle Länder wählbar (Fallback: Deutsch)
      }
    })();
  }, []);

  useEffect(() => {
    const saved = localStorage.getItem("fragebogen_country");
    const found = saved && COUNTRIES.find((c) => c.code === saved);
    if (found) {
      setCountry(found.code);
      setLang(found.lang);
    }
  }, []);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const t = await fetchTranslation(lang);
      if (!cancelled) setTranslation(t);
    })();
    return () => {
      cancelled = true;
    };
  }, [lang]);

  const handleCountryChange = (code: string, language: string) => {
    setCountry(code);
    setLang(language);
    localStorage.setItem("fragebogen_country", code);
  };

  const ui = uiStrings(translation);
  const dir = RTL_LANGUAGES.has(lang) ? "rtl" : "ltr";

  const schema = sessionData?.template;
  const hasV2Schema = isV2Schema(schema);
  const translatedSchema = useMemo(
    () => (hasV2Schema ? translateSchema(schema, translation) : schema),
    [schema, hasV2Schema, translation]
  );

  // DGUV-Kataloge tragen ihren eigenen (deutschen) Titel; nur die Verkehrs-
  // medizin nutzt den übersetzten i18n-Titel
  const schemaTitle: string | undefined = hasV2Schema ? schema?.title : undefined;
  const istVerkehrsmedizin =
    !schemaTitle || schemaTitle.toLowerCase().includes("verkehrsmedizin");
  const headerTitle = istVerkehrsmedizin ? ui.header_title : schemaTitle;

  useEffect(() => {
    if (!istVerkehrsmedizin && schemaTitle) document.title = schemaTitle;
  }, [istVerkehrsmedizin, schemaTitle]);

  useEffect(() => {
    if (!token) return;
    (async () => {
      try {
        const res = await fetch(`${API_URL}/api/session/${token}/`);
        if (!res.ok) {
          const d = await res.json();
          throw new Error(d.error || "Fragebogen nicht gefunden");
        }
        setSessionData(await res.json());
      } catch (e: any) {
        setError(e.message || "Unbekannter Fehler");
      } finally {
        setLoading(false);
      }
    })();
  }, [token]);

  const handleSubmit = async (data: Record<string, unknown>) => {
    setIsSubmitting(true);
    try {
      const res = await fetch(`${API_URL}/api/submit/${token}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) {
        const d = await res.json().catch(() => ({}));
        throw new Error(extractApiError(d));
      }
      const json = await res.json();
      setResult(json);
      setSubmitted(true);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (e: any) {
      toast.error(e.message || "Fehler beim Absenden. Bitte versuchen Sie es erneut.");
    } finally {
      setIsSubmitting(false);
    }
  };

  // ── Loading ────────────────────────────────────────────────────────────────
  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <Spinner className="size-10 text-primary mx-auto mb-4" />
          <p className="text-sm text-muted-foreground">{ui.loading}</p>
        </div>
      </main>
    );
  }

  // ── Error ──────────────────────────────────────────────────────────────────
  if (error) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-background p-4">
        <Card className="max-w-md w-full text-center">
          <CardContent className="p-8">
            <AlertCircle className="size-12 text-destructive mx-auto mb-4" />
            <h2 className="text-lg font-semibold text-foreground mb-2">Fragebogen nicht gefunden</h2>
            <p className="text-sm text-muted-foreground mb-6">{error}</p>
            <Button onClick={() => router.push("/")}>Zur Startseite</Button>
          </CardContent>
        </Card>
      </main>
    );
  }

  // ── Success ────────────────────────────────────────────────────────────────
  if (submitted && result) {
    const band = result.ess_band || "normal";
    const bandMeta: Record<string, { box: string; text: string; badgeVariant: "success" | "warning" | "destructive"; label: string }> = {
      normal:     { box: "border-success/50 bg-success/10",         text: "text-success",     badgeVariant: "success",     label: ui.band_normal },
      erhöht:     { box: "border-warning/50 bg-warning/10",         text: "text-warning",     badgeVariant: "warning",     label: ui.band_elevated },
      ausgeprägt: { box: "border-destructive/50 bg-destructive/10", text: "text-destructive", badgeVariant: "destructive", label: ui.band_severe },
    };
    const m = bandMeta[band] ?? bandMeta["normal"];

    return (
      <main className="min-h-screen bg-background flex items-center justify-center p-4" dir={dir}>
        <div className="max-w-lg w-full space-y-4">
          <Card>
            <CardContent className="p-8 text-center">
              <div className="mx-auto mb-4 flex size-16 items-center justify-center rounded-full bg-success/15">
                <CheckCircle2 className="size-8 text-success" />
              </div>
              <h1 className="text-xl font-bold text-foreground mb-1">{ui.success_title}</h1>
              <p className="text-sm text-muted-foreground">{ui.success_text}</p>
            </CardContent>
          </Card>

          {result.ess_total !== null && result.ess_total !== undefined && (
            <div className={cn("rounded-xl border-2 p-6", m.box)}>
              <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-3">{ui.success_result}</p>
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-4xl font-black text-foreground">{result.ess_total}</span>
                  <span className="text-lg text-muted-foreground ml-1">/ 24</span>
                  <p className={cn("text-sm font-semibold mt-1", m.text)}>{m.label}</p>
                </div>
                <div className={cn(badgeVariants({ variant: m.badgeVariant }), "flex size-16 items-center justify-center rounded-full border-0 text-2xl font-black")}>
                  {result.ess_total}
                </div>
              </div>
              <p className="mt-4 text-xs text-muted-foreground">{ui.success_doctor_note}</p>
            </div>
          )}

          <Button
            className="h-12 w-full gap-2 text-sm"
            onClick={() => window.open(`/api/puppeteer-pdf/${token}/`, "_blank")}
          >
            <Download className="size-4" />
            {ui.success_pdf}
          </Button>

          <p className="text-center text-xs text-muted-foreground">{ui.success_close}</p>
        </div>
      </main>
    );
  }

  // ── Form ───────────────────────────────────────────────────────────────────
  return (
    <main className="min-h-screen bg-background">
      {/* Sticky header */}
      <header className="bg-card border-b border-border sticky top-0 z-20 shadow-sm">
        <div className="max-w-3xl mx-auto px-4 py-3 flex items-center gap-3">
          <div className="flex size-8 shrink-0 items-center justify-center rounded-lg bg-primary">
            {istVerkehrsmedizin ? (
              <Car className="size-4 text-primary-foreground" />
            ) : (
              <Stethoscope className="size-4 text-primary-foreground" />
            )}
          </div>
          <div className="min-w-0 flex-1">
            <h1 className="text-sm font-semibold text-foreground truncate">
              {headerTitle}
            </h1>
            <p className="text-xs text-muted-foreground truncate">
              {ui.header_subtitle}
            </p>
          </div>
          <LanguageSelect
            value={country}
            onSelect={handleCountryChange}
            label={ui.language_label}
            available={availableLangs}
          />
          <ModeToggle />
        </div>
      </header>

      {/* Form body – edge-to-edge on mobile, Card on sm+ */}
      <div className="max-w-3xl mx-auto py-4 pb-20" dir={dir}>
        <div className="sm:px-4">
          <Card className="rounded-none border-x-0 border-t-0 sm:rounded-xl sm:border shadow-none sm:shadow-sm">
            <CardContent className="p-4 sm:p-8">
              {hasV2Schema ? (
                <AnamneseForm
                  schema={translatedSchema}
                  onSubmit={handleSubmit}
                  isSubmitting={isSubmitting}
                  ui={ui}
                />
              ) : (
                <div className="py-8 text-center space-y-2">
                  <AlertCircle className="size-10 text-muted-foreground mx-auto" />
                  <h2 className="text-lg font-semibold text-foreground">Veraltete Vorlage</h2>
                  <p className="text-sm text-muted-foreground">
                    Dieser Fragebogen-Link gehört zu einer veralteten Vorlage und kann online
                    nicht mehr ausgefüllt werden. Bitte wenden Sie sich an die Praxis, um einen
                    neuen Link zu erhalten.
                  </p>
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </main>
  );
}
