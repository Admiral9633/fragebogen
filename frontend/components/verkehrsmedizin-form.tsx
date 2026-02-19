"use client";

import { useState } from "react";
import { cn } from "@/lib/utils";
import { calcESS, ESS_QUESTIONS } from "@/lib/ess";
import { Progress } from "@/components/ui/progress";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { ChevronLeft, ChevronRight } from "lucide-react";

export type FormData = Record<string, any>;

interface VerkehrsmedizinFormProps {
  onSubmit: (data: FormData) => Promise<void>;
  isSubmitting: boolean;
}

// --- Step definitions --------------------------------------------------------

const STEPS = [
  { id: "fahrprofil",   title: "Fahrprofil",                  subtitle: "Angaben zu Ihrer Fahrtätigkeit" },
  { id: "warnsymptome", title: "Warnsymptome",                subtitle: "Plötzliches Ausfallrisiko" },
  { id: "sehen",        title: "Sehen & Hören",               subtitle: "Seh- und Hörfunktion" },
  { id: "herz",         title: "Herz-Kreislauf",              subtitle: "Kardiovaskuläre Erkrankungen" },
  { id: "neuro",        title: "Neurologie",                  subtitle: "Neurologische Erkrankungen" },
  { id: "diabetes",     title: "Diabetes / Stoffwechsel",     subtitle: "Blutzucker und Therapie" },
  { id: "schlaf",       title: "Schlaf & Tagesschläfrigkeit", subtitle: "Inkl. Epworth Sleepiness Scale (ESS)" },
  { id: "psyche",       title: "Psychische Gesundheit",       subtitle: "Psychiatrische Erkrankungen" },
  { id: "substanzen",   title: "Substanzen & Medikamente",    subtitle: "Alkohol, Drogen, Medikamente" },
  { id: "einwilligung", title: "Einwilligung",                subtitle: "Erklärung & Datenschutz" },
];

// --- Per-step Validation -----------------------------------------------------

function validateStep(step: number, data: FormData): Record<string, string> {
  const errors: Record<string, string> = {};
  const req = (key: string, label: string) => {
    if (!data[key] && data[key] !== 0) errors[key] = `${label} ist erforderlich`;
  };

  switch (step) {
    case 0:
      req("license_classes", "Führerscheinklasse");
      req("driving_hours", "Fahrzeit pro Tag");
      req("night_driving", "Nachtfahrten");
      req("accidents", "Unfälle / Beinahe-Unfälle");
      break;
    case 1:
      req("syncope", "Ohnmacht/Bewusstlosigkeit");
      req("seizures", "Krampfanfälle");
      req("dizziness", "Schwindelattacken");
      req("neuro_deficit", "Neurologische Ausfälle");
      break;
    case 2:
      req("glasses", "Brille/Kontaktlinsen");
      req("vision_problems", "Sehprobleme");
      req("hearing_aid", "Hörgerät");
      break;
    case 3:
      req("heart_attack", "Herzinfarkt");
      req("arrhythmia", "Rhythmusstörungen");
      req("heart_failure", "Herzinsuffizienz");
      break;
    case 4:
      req("epilepsy", "Epilepsie");
      req("parkinson", "Parkinson");
      req("ms", "Multiple Sklerose");
      req("migraine_aura", "Migräne mit Aura");
      break;
    case 5:
      req("diabetes_type", "Diabetes");
      req("hypoglycemia", "Hypoglykämie mit Fremdhilfe");
      break;
    case 6:
      req("daytime_sleepiness", "Tagesmüdigkeit");
      req("microsleep", "Sekundenschlaf");
      req("snoring", "Schnarchen / Atemaussetzer");
      for (let i = 1; i <= 8; i++) {
        if (data[`ess_${i}`] === undefined || data[`ess_${i}`] === "") {
          errors[`ess_${i}`] = "Bitte auswählen";
        }
      }
      break;
    case 7:
      req("psychiatric", "Psychiatrische Erkrankung");
      req("concentration", "Konzentrations-/Gedächtnisprobleme");
      break;
    case 8:
      req("alcohol", "Alkohol");
      req("drugs", "Drogenkonsum");
      req("sedating_meds", "Sedierende Medikamente");
      break;
    case 9:
      if (!data.consent_truth) errors.consent_truth = "Pflichtfeld";
      if (!data.consent_privacy) errors.consent_privacy = "Pflichtfeld";
      break;
  }
  return errors;
}

// --- Shared sub-components ---------------------------------------------------

function QuestionBlock({
  label, hint, required, error, children,
}: {
  label: string; hint?: string; required?: boolean; error?: string; children: React.ReactNode;
}) {
  return (
    <div className="space-y-3">
      <div>
        <p className="text-sm font-semibold text-foreground">
          {label}
          {required && <span className="text-red-500 ml-0.5"> *</span>}
        </p>
        {hint && <p className="text-xs text-muted-foreground mt-0.5">{hint}</p>}
      </div>
      <div>{children}</div>
      {error && <p className="text-xs text-red-500">{error}</p>}
    </div>
  );
}

function YesNoGroup({
  name, value, onChange,
}: {
  name: string; value?: string; onChange: (v: string) => void; error?: string;
}) {
  return (
    <RadioGroup name={name} value={value} onValueChange={onChange} orientation="horizontal">
      <RadioGroupItem value="yes" label="Ja" />
      <RadioGroupItem value="no" label="Nein" />
    </RadioGroup>
  );
}

// --- Main Component ----------------------------------------------------------

export function VerkehrsmedizinForm({ onSubmit, isSubmitting }: VerkehrsmedizinFormProps) {
  const [step, setStep] = useState(0);
  const [data, setData] = useState<FormData>({});
  const [errors, setErrors] = useState<Record<string, string>>({});

  const set = (key: string, value: any) => {
    setData((prev) => ({ ...prev, [key]: value }));
    setErrors((prev) => { const n = { ...prev }; delete n[key]; return n; });
  };

  const { total: essTotal, band: essBand, bandLabel: essBandLabel } = calcESS(data);

  const goNext = async () => {
    const errs = validateStep(step, data);
    if (Object.keys(errs).length > 0) {
      setErrors(errs);
      window.scrollTo({ top: 0, behavior: "smooth" });
      return;
    }
    setErrors({});
    if (step === STEPS.length - 1) {
      await onSubmit({ ...data, ess_total: essTotal, ess_band: essBand });
    } else {
      setStep((s) => s + 1);
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const goBack = () => {
    setErrors({});
    setStep((s) => s - 1);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const currentStep = STEPS[step];
  const progressValue = ((step + 1) / STEPS.length) * 100;
  const hasErrors = Object.keys(errors).length > 0;

  return (
    <div className="space-y-6">
      {/* Progress bar */}
      <div className="space-y-2">
        <Progress value={progressValue} className="h-1.5" />
        <p className="text-xs text-muted-foreground text-right">
          Schritt {step + 1} von {STEPS.length}
        </p>
      </div>

      {/* Step header */}
      <div>
        <h2 className="text-2xl font-bold text-foreground">{currentStep.title}</h2>
        <p className="text-sm text-muted-foreground mt-1">{currentStep.subtitle}</p>
      </div>

      {/* Error summary */}
      {hasErrors && (
        <div className="rounded-lg border border-red-200 bg-red-50 dark:border-red-800 dark:bg-red-900/20 px-4 py-3">
          <p className="text-sm font-medium text-red-700 dark:text-red-400">
            {Object.keys(errors).length} Feld
            {Object.keys(errors).length !== 1 ? "er fehlen" : " fehlt"} noch.
            Bitte prüfen Sie Ihre Angaben.
          </p>
        </div>
      )}

      {/* Step content */}
      <div className="space-y-6">
        {step === 0 && <StepFahrprofil    data={data} errors={errors} set={set} />}
        {step === 1 && <StepWarnsymptome  data={data} errors={errors} set={set} />}
        {step === 2 && <StepSehenHoeren   data={data} errors={errors} set={set} />}
        {step === 3 && <StepHerz          data={data} errors={errors} set={set} />}
        {step === 4 && <StepNeuro         data={data} errors={errors} set={set} />}
        {step === 5 && <StepDiabetes      data={data} errors={errors} set={set} />}
        {step === 6 && (
          <StepSchlaf
            data={data} errors={errors} set={set}
            essTotal={essTotal} essBand={essBand} essBandLabel={essBandLabel}
          />
        )}
        {step === 7 && <StepPsyche        data={data} errors={errors} set={set} />}
        {step === 8 && <StepSubstanzen    data={data} errors={errors} set={set} />}
        {step === 9 && <StepEinwilligung  data={data} errors={errors} set={set} />}
      </div>

      {/* Navigation */}
      <div className="flex items-center justify-between pt-2 pb-4">
        <Button
          type="button"
          variant="outline"
          onClick={goBack}
          disabled={step === 0}
          className="gap-1"
        >
          <ChevronLeft className="w-4 h-4" />
          Zurück
        </Button>
        <Button
          type="button"
          onClick={goNext}
          disabled={isSubmitting}
          className="gap-1 min-w-[120px]"
        >
          {isSubmitting ? (
            <span className="flex items-center gap-2">
              <span className="w-4 h-4 border-2 border-white/40 border-t-white rounded-full animate-spin" />
              Senden...
            </span>
          ) : step === STEPS.length - 1 ? (
            "Absenden"
          ) : (
            <>
              Weiter
              <ChevronRight className="w-4 h-4" />
            </>
          )}
        </Button>
      </div>
    </div>
  );
}

// --- Step Components ---------------------------------------------------------

type StepProps = {
  data: FormData;
  errors: Record<string, string>;
  set: (key: string, value: any) => void;
};

function StepFahrprofil({ data, errors, set }: StepProps) {
  const LICENSE_CLASSES = ["AM","A1","A2","A","B","BE","C1","C1E","C","CE","D1","D","T"];
  return (
    <div className="space-y-6">
      <QuestionBlock label="Führerscheinklassen" required error={errors.license_classes}>
        <div className="flex flex-wrap gap-2">
          {LICENSE_CLASSES.map((cls) => (
            <button
              key={cls}
              type="button"
              onClick={() => {
                const cur: string[] = data.license_classes_arr || [];
                const next = cur.includes(cls)
                  ? cur.filter((x) => x !== cls)
                  : [...cur, cls];
                set("license_classes_arr", next);
                set("license_classes", next.join(", "));
              }}
              className={cn(
                "px-3 py-1.5 rounded-lg border-2 text-xs font-semibold transition-all",
                (data.license_classes_arr || []).includes(cls)
                  ? "border-primary bg-primary text-primary-foreground"
                  : "border-border bg-card text-muted-foreground hover:border-border/60"
              )}
            >
              {cls}
            </button>
          ))}
        </div>
      </QuestionBlock>

      <QuestionBlock label="Fahrzeit pro Tag (Stunden)" required error={errors.driving_hours}>
        <RadioGroup
          name="driving_hours"
          value={data.driving_hours}
          onValueChange={(v) => set("driving_hours", v)}
          orientation="horizontal"
        >
          <RadioGroupItem value="<1"  label="&lt; 1 h" />
          <RadioGroupItem value="1-2" label="1-2 h" />
          <RadioGroupItem value="2-4" label="2-4 h" />
          <RadioGroupItem value=">4"  label="&gt; 4 h" />
        </RadioGroup>
      </QuestionBlock>

      <QuestionBlock label="Regelmäßige Nachtfahrten" required error={errors.night_driving}>
        <YesNoGroup name="night_driving" value={data.night_driving} onChange={(v) => set("night_driving", v)} />
      </QuestionBlock>

      <QuestionBlock
        label="Unfälle oder Beinahe-Unfälle in den letzten 24 Monaten"
        required
        error={errors.accidents}
      >
        <YesNoGroup name="accidents" value={data.accidents} onChange={(v) => set("accidents", v)} />
        {data.accidents === "yes" && (
          <div className="mt-3">
            <Textarea
              placeholder="Kurze Beschreibung"
              value={data.accidents_desc || ""}
              onChange={(e) => set("accidents_desc", e.target.value)}
            />
          </div>
        )}
      </QuestionBlock>
    </div>
  );
}

function StepWarnsymptome({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-6">
      <QuestionBlock
        label="Ohnmacht oder Bewusstlosigkeit in den letzten 5 Jahren"
        required
        error={errors.syncope}
      >
        <YesNoGroup name="syncope" value={data.syncope} onChange={(v) => set("syncope", v)} />
      </QuestionBlock>
      <QuestionBlock label="Krampfanfälle oder epileptische Anfälle" required error={errors.seizures}>
        <YesNoGroup name="seizures" value={data.seizures} onChange={(v) => set("seizures", v)} />
      </QuestionBlock>
      <QuestionBlock label="Schwindelattacken" required error={errors.dizziness}>
        <YesNoGroup name="dizziness" value={data.dizziness} onChange={(v) => set("dizziness", v)} />
      </QuestionBlock>
      <QuestionBlock
        label="Neurologische Ausfälle (z.B. Lähmung, Sprachstörung)"
        required
        error={errors.neuro_deficit}
      >
        <YesNoGroup name="neuro_deficit" value={data.neuro_deficit} onChange={(v) => set("neuro_deficit", v)} />
      </QuestionBlock>
    </div>
  );
}

function StepSehenHoeren({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-6">
      <QuestionBlock label="Brille oder Kontaktlinsen" required error={errors.glasses}>
        <YesNoGroup name="glasses" value={data.glasses} onChange={(v) => set("glasses", v)} />
      </QuestionBlock>
      <QuestionBlock
        label="Sehprobleme"
        hint="Doppeltsehen, Gesichtsfeldausfälle, Nachtsehen"
        required
        error={errors.vision_problems}
      >
        <YesNoGroup
          name="vision_problems"
          value={data.vision_problems}
          onChange={(v) => set("vision_problems", v)}
        />
        {data.vision_problems === "yes" && (
          <div className="mt-3">
            <Textarea
              placeholder="Art der Sehprobleme beschreiben"
              value={data.vision_desc || ""}
              onChange={(e) => set("vision_desc", e.target.value)}
            />
          </div>
        )}
      </QuestionBlock>
      <QuestionBlock label="Hörgerät oder relevante Hörstörung" required error={errors.hearing_aid}>
        <YesNoGroup name="hearing_aid" value={data.hearing_aid} onChange={(v) => set("hearing_aid", v)} />
      </QuestionBlock>
    </div>
  );
}

function StepHerz({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-6">
      <QuestionBlock label="Herzinfarkt oder koronare Erkrankung" required error={errors.heart_attack}>
        <YesNoGroup name="heart_attack" value={data.heart_attack} onChange={(v) => set("heart_attack", v)} />
      </QuestionBlock>
      <QuestionBlock label="Rhythmusstörungen, Schrittmacher oder ICD" required error={errors.arrhythmia}>
        <YesNoGroup name="arrhythmia" value={data.arrhythmia} onChange={(v) => set("arrhythmia", v)} />
      </QuestionBlock>
      <QuestionBlock label="Herzinsuffizienz" required error={errors.heart_failure}>
        <YesNoGroup name="heart_failure" value={data.heart_failure} onChange={(v) => set("heart_failure", v)} />
      </QuestionBlock>
      <QuestionBlock label="Synkopenabklärung bereits erfolgt?">
        <YesNoGroup name="syncope_workup" value={data.syncope_workup} onChange={(v) => set("syncope_workup", v)} />
      </QuestionBlock>
    </div>
  );
}

function StepNeuro({ data, errors, set }: StepProps) {
  const questions = [
    { k: "epilepsy",         l: "Epilepsie",                req: true  },
    { k: "parkinson",        l: "Parkinson",                req: true  },
    { k: "ms",               l: "Multiple Sklerose (MS)",   req: true  },
    { k: "migraine_aura",    l: "Migräne mit Aura",          req: true  },
    { k: "balance_disorder", l: "Gleichgewichtsstörungen",   req: false },
  ];
  return (
    <div className="space-y-6">
      {questions.map(({ k, l, req }) => (
        <QuestionBlock key={k} label={l} required={req} error={errors[k]}>
          <YesNoGroup name={k} value={data[k]} onChange={(v) => set(k, v)} />
        </QuestionBlock>
      ))}
    </div>
  );
}

function StepDiabetes({ data, errors, set }: StepProps) {
  const hasDiabetes = data.diabetes_type && data.diabetes_type !== "none";
  return (
    <div className="space-y-6">
      <QuestionBlock label="Diabetesform" required error={errors.diabetes_type}>
        <RadioGroup
          name="diabetes_type"
          value={data.diabetes_type}
          onValueChange={(v) => set("diabetes_type", v)}
          orientation="horizontal"
        >
          <RadioGroupItem value="none"  label="Kein Diabetes" />
          <RadioGroupItem value="type1" label="Typ 1" />
          <RadioGroupItem value="type2" label="Typ 2" />
        </RadioGroup>
      </QuestionBlock>

      <QuestionBlock
        label="Hypoglykämie mit Fremdhilfe in den letzten 12 Monaten"
        required
        error={errors.hypoglycemia}
      >
        <YesNoGroup name="hypoglycemia" value={data.hypoglycemia} onChange={(v) => set("hypoglycemia", v)} />
      </QuestionBlock>

      {hasDiabetes && (
        <>
          <QuestionBlock label="Hypowahrnehmungsstörung">
            <YesNoGroup
              name="hypo_awareness"
              value={data.hypo_awareness}
              onChange={(v) => set("hypo_awareness", v)}
            />
          </QuestionBlock>
          <QuestionBlock label="Aktuelle Therapie">
            <RadioGroup
              name="diabetes_therapy"
              value={data.diabetes_therapy}
              onValueChange={(v) => set("diabetes_therapy", v)}
              orientation="horizontal"
            >
              <RadioGroupItem value="insulin"  label="Insulin" />
              <RadioGroupItem value="tablets"  label="Tabletten" />
              <RadioGroupItem value="diet"     label="Diät" />
              <RadioGroupItem value="other"    label="Sonstige" />
            </RadioGroup>
          </QuestionBlock>
        </>
      )}
    </div>
  );
}

function StepSchlaf({
  data, errors, set, essTotal, essBand, essBandLabel,
}: StepProps & { essTotal: number; essBand: string; essBandLabel: string }) {
  const bandClass =
    essBand === "ausgeprägt" ? "border-red-200 bg-red-50"
    : essBand === "erhöht"   ? "border-orange-200 bg-orange-50"
    :                           "border-green-200 bg-green-50";
  const badgeClass =
    essBand === "ausgeprägt" ? "bg-red-500"
    : essBand === "erhöht"   ? "bg-orange-400"
    :                           "bg-green-500";
  const textClass =
    essBand === "ausgeprägt" ? "text-red-700"
    : essBand === "erhöht"   ? "text-orange-700"
    :                           "text-green-700";

  return (
    <div className="space-y-6">
      <QuestionBlock label="Ausgeprägte Tagesmüdigkeit" required error={errors.daytime_sleepiness}>
        <YesNoGroup
          name="daytime_sleepiness"
          value={data.daytime_sleepiness}
          onChange={(v) => set("daytime_sleepiness", v)}
        />
      </QuestionBlock>
      <QuestionBlock label="Sekundenschlaf beim Fahren" required error={errors.microsleep}>
        <YesNoGroup name="microsleep" value={data.microsleep} onChange={(v) => set("microsleep", v)} />
      </QuestionBlock>
      <QuestionBlock label="Schnarchen oder Atemaussetzer" required error={errors.snoring}>
        <YesNoGroup name="snoring" value={data.snoring} onChange={(v) => set("snoring", v)} />
      </QuestionBlock>

      {/* ESS Sub-block */}
      <div className="rounded-xl border border-blue-200 bg-blue-50/50 dark:border-blue-900/50 dark:bg-blue-950/20 p-4 space-y-5">
        <div>
          <p className="text-sm font-semibold text-blue-900 dark:text-blue-100">Epworth Sleepiness Scale (ESS)</p>
          <p className="text-xs text-blue-700 dark:text-blue-300 mt-1">
            Wie wahrscheinlich ist es, dass Sie in den folgenden Situationen einnicken würden?
          </p>
          <p className="text-xs text-blue-600 dark:text-blue-400 font-medium mt-0.5">
            0 = Nie &nbsp;&middot;&nbsp; 1 = Gering &nbsp;&middot;&nbsp; 2 = Mittel &nbsp;&middot;&nbsp; 3 = Hoch
          </p>
        </div>

        {ESS_QUESTIONS.map((q, i) => (
          <div key={q.id} className="space-y-2">
            <Label className="text-xs font-medium text-foreground/80">
              {i + 1}. {q.text}
            </Label>
            <RadioGroup
              name={q.id}
              value={data[q.id] !== undefined ? String(data[q.id]) : undefined}
              onValueChange={(v) => set(q.id, parseInt(v))}
              orientation="horizontal"
              error={errors[q.id]}
            >
              {[0, 1, 2, 3].map((n) => (
                <RadioGroupItem key={n} value={String(n)} label={String(n)} />
              ))}
            </RadioGroup>
          </div>
        ))}

        {/* ESS Score Box */}
        <div className={cn("rounded-xl border-2 p-4 flex items-center justify-between", bandClass)}>
          <div>
            <p className="text-2xl font-bold text-foreground">
              {essTotal}{" "}
              <span className="text-base font-normal text-muted-foreground">/ 24 Punkte</span>
            </p>
            <p className={cn("text-sm font-semibold mt-0.5", textClass)}>{essBandLabel}</p>
          </div>
          <div
            className={cn(
              "w-14 h-14 rounded-full flex items-center justify-center text-xl font-black text-white",
              badgeClass
            )}
          >
            {essTotal}
          </div>
        </div>
      </div>
    </div>
  );
}

function StepPsyche({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-6">
      <QuestionBlock
        label="Depression, Angststörung oder andere psychiatrische Erkrankung"
        required
        error={errors.psychiatric}
      >
        <YesNoGroup name="psychiatric" value={data.psychiatric} onChange={(v) => set("psychiatric", v)} />
        {data.psychiatric === "yes" && (
          <div className="mt-3">
            <Input
              placeholder="Art der Erkrankung"
              value={data.psychiatric_desc || ""}
              onChange={(e) => set("psychiatric_desc", e.target.value)}
            />
          </div>
        )}
      </QuestionBlock>
      <QuestionBlock label="Stationäre psychiatrische Behandlung in den letzten 5 Jahren">
        <YesNoGroup
          name="psychiatric_inpatient"
          value={data.psychiatric_inpatient}
          onChange={(v) => set("psychiatric_inpatient", v)}
        />
      </QuestionBlock>
      <QuestionBlock label="Konzentrations- oder Gedächtnisprobleme" required error={errors.concentration}>
        <YesNoGroup name="concentration" value={data.concentration} onChange={(v) => set("concentration", v)} />
      </QuestionBlock>
    </div>
  );
}

function StepSubstanzen({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-6">
      <QuestionBlock
        label="Alkohol"
        hint="Regelmäßiger oder riskanter Konsum"
        required
        error={errors.alcohol}
      >
        <RadioGroup
          name="alcohol"
          value={data.alcohol}
          onValueChange={(v) => set("alcohol", v)}
          orientation="horizontal"
        >
          <RadioGroupItem value="none"       label="Keinen" />
          <RadioGroupItem value="occasional" label="Gelegentlich" />
          <RadioGroupItem value="regular"    label="Regelmäßig" />
          <RadioGroupItem value="risky"      label="Riskant" />
        </RadioGroup>
      </QuestionBlock>

      <QuestionBlock label="Drogenkonsum aktuell oder früher" required error={errors.drugs}>
        <YesNoGroup name="drugs" value={data.drugs} onChange={(v) => set("drugs", v)} />
        {data.drugs === "yes" && (
          <div className="mt-3">
            <Input
              placeholder="Art und Zeitraum"
              value={data.drugs_desc || ""}
              onChange={(e) => set("drugs_desc", e.target.value)}
            />
          </div>
        )}
      </QuestionBlock>

      <QuestionBlock label="Medikamente mit sedierender Wirkung" required error={errors.sedating_meds}>
        <YesNoGroup name="sedating_meds" value={data.sedating_meds} onChange={(v) => set("sedating_meds", v)} />
        {data.sedating_meds === "yes" && (
          <div className="mt-3">
            <Input
              placeholder="Welche Medikamente?"
              value={data.sedating_meds_desc || ""}
              onChange={(e) => set("sedating_meds_desc", e.target.value)}
            />
          </div>
        )}
      </QuestionBlock>

      <QuestionBlock label="Nebenwirkungen wie Schläfrigkeit oder Schwindel">
        <YesNoGroup name="side_effects" value={data.side_effects} onChange={(v) => set("side_effects", v)} />
      </QuestionBlock>
    </div>
  );
}

function StepEinwilligung({ data, errors, set }: StepProps) {
  return (
    <div className="space-y-4">
      <p className="text-sm text-muted-foreground">
        Bitte bestätigen Sie die folgenden Erklärungen, um den Fragebogen abzusenden.
      </p>
      <Checkbox
        id="consent_truth"
        label={
          <span>
            Ich bestätige, dass meine Angaben{" "}
            <strong>vollständig und wahrheitsgemäß</strong> sind.
          </span>
        }
        checked={!!data.consent_truth}
        onChange={(e) => set("consent_truth", (e.target as HTMLInputElement).checked)}
        error={errors.consent_truth}
      />
      <Checkbox
        id="consent_privacy"
        label={
          <span>
            Ich habe die <strong>Datenschutzhinweise</strong> gelesen und willige in die
            Verarbeitung meiner Daten zu verkehrsmedizinischen Zwecken ein.
          </span>
        }
        checked={!!data.consent_privacy}
        onChange={(e) => set("consent_privacy", (e.target as HTMLInputElement).checked)}
        error={errors.consent_privacy}
      />
      <p className="text-xs text-muted-foreground/60 pt-2 text-center">
        Ihre Daten werden verschlüsselt und DSGVO-konform übertragen.
      </p>
    </div>
  );
}
