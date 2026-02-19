"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { VerkehrsmedizinForm, FormData } from "@/components/verkehrsmedizin-form";
import { CheckCircle2, AlertCircle, Download, FileText, Car } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ThemeToggle } from "@/components/theme-toggle";

const API_URL = ""; // Requests go via Next.js proxy rewrites → backend:8000

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

  const handleSubmit = async (data: FormData) => {
    setIsSubmitting(true);
    try {
      const res = await fetch(`${API_URL}/api/submit/${token}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) {
        const d = await res.json();
        throw new Error(JSON.stringify(d));
      }
      const json = await res.json();
      setResult(json);
      setSubmitted(true);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (e: any) {
      alert("Fehler beim Absenden: " + e.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // ── Loading ────────────────────────────────────────────────────────────────
  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <div className="w-10 h-10 border-4 border-primary/20 border-t-primary rounded-full animate-spin mx-auto mb-4" />
          <p className="text-sm text-muted-foreground">Lade Fragebogen …</p>
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
            <AlertCircle className="w-12 h-12 text-destructive mx-auto mb-4" />
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
    const bandMeta: Record<string, { bg: string; border: string; text: string; badge: string; label: string }> = {
      normal:     { bg: "bg-green-50 dark:bg-green-950/30",   border: "border-green-200 dark:border-green-800",   text: "text-green-700 dark:text-green-400",   badge: "bg-green-500",  label: "Normal (0–9)" },
      erhöht:     { bg: "bg-orange-50 dark:bg-orange-950/30", border: "border-orange-200 dark:border-orange-800", text: "text-orange-700 dark:text-orange-400", badge: "bg-orange-400", label: "Erhöht (10–15)" },
      ausgeprägt: { bg: "bg-red-50 dark:bg-red-950/30",       border: "border-red-200 dark:border-red-800",       text: "text-red-700 dark:text-red-400",       badge: "bg-red-500",    label: "Ausgeprägt (≥16)" },
    };
    const m = bandMeta[band] ?? bandMeta["normal"];

    return (
      <main className="min-h-screen bg-background flex items-center justify-center p-4">
        <div className="max-w-lg w-full space-y-4">
          <Card>
            <CardContent className="p-8 text-center">
              <div className="w-16 h-16 bg-green-100 dark:bg-green-900/40 rounded-full flex items-center justify-center mx-auto mb-4">
                <CheckCircle2 className="w-8 h-8 text-green-600 dark:text-green-400" />
              </div>
              <h1 className="text-xl font-bold text-foreground mb-1">Vielen Dank!</h1>
              <p className="text-sm text-muted-foreground">Ihr Fragebogen wurde erfolgreich übermittelt.</p>
            </CardContent>
          </Card>

          <div className={cn("rounded-xl border-2 p-6", m.bg, m.border)}>
            <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-3">ESS-Ergebnis</p>
            <div className="flex items-center justify-between">
              <div>
                <span className="text-4xl font-black text-foreground">{result.ess_total}</span>
                <span className="text-lg text-muted-foreground ml-1">/ 24</span>
                <p className={cn("text-sm font-semibold mt-1", m.text)}>{m.label}</p>
              </div>
              <div className={cn("w-16 h-16 rounded-full flex items-center justify-center text-white text-2xl font-black", m.badge)}>
                {result.ess_total}
              </div>
            </div>
            <p className="mt-4 text-xs text-muted-foreground">
              Bitte besprechen Sie das Ergebnis mit Ihrem Arzt. Eine abschließende Bewertung erfolgt durch einen Facharzt.
            </p>
          </div>

          <div className="flex gap-3">
            <Button
              variant="outline"
              className="flex-1 h-12 gap-2 text-sm"
              onClick={() => window.open(`${API_URL}/api/pdf/${token}/`, "_blank")}
            >
              <FileText className="w-4 h-4" />
              PDF (klassisch)
            </Button>
            <Button
              className="flex-1 h-12 gap-2 text-sm"
              onClick={() => window.open(`/api/puppeteer-pdf/${token}/`, "_blank")}
            >
              <Download className="w-4 h-4" />
              PDF (Design)
            </Button>
          </div>

          <p className="text-center text-xs text-muted-foreground">Sie können dieses Fenster nun schließen.</p>
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
          <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center flex-shrink-0">
            <Car className="w-4 h-4 text-primary-foreground" />
          </div>
          <div className="min-w-0 flex-1">
            <h1 className="text-sm font-semibold text-foreground truncate">
              Verkehrsmedizinischer Fragebogen
            </h1>
            <p className="text-xs text-muted-foreground truncate">
              {sessionData?.template?.title || "Bitte füllen Sie alle Felder aus"}
            </p>
          </div>
          <ThemeToggle />
        </div>
      </header>

      {/* Form body – edge-to-edge on mobile, Card on sm+ */}
      <div className="max-w-3xl mx-auto py-4 pb-20">
        <div className="sm:px-4">
          <Card className="rounded-none border-x-0 border-t-0 sm:rounded-xl sm:border shadow-none sm:shadow-sm">
            <CardContent className="p-4 sm:p-8">
              <VerkehrsmedizinForm onSubmit={handleSubmit} isSubmitting={isSubmitting} />
            </CardContent>
          </Card>
        </div>
      </div>
    </main>
  );
}