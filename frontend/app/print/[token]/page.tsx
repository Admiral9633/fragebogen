import { notFound } from "next/navigation";
import fs from "fs";
import path from "path";
import { ESS_QUESTIONS } from "@/lib/ess";
import {
  answerDisplay,
  isV2Schema,
  isVisible,
  type Question,
  type Schema,
  type Section as SchemaSection,
} from "@/lib/schema";

const BACKEND_URL = process.env.BACKEND_URL || "http://backend:8000";

function getLogoDataUrl(): string {
  try {
    const logoPath = path.join(process.cwd(), "public", "logo.svg");
    const svg = fs.readFileSync(logoPath, "utf-8");
    return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
  } catch {
    return "";
  }
}

interface AnswerData {
  answers: Record<string, unknown>;
  schema?: unknown;
  ess_total: number;
  ess_band: string;
  completed_at: string | null;
  token: string;
  patient_last_name: string;
  patient_first_name: string;
  patient_birth_date: string;
}

async function getAnswerData(token: string): Promise<AnswerData | null> {
  try {
    const res = await fetch(`${BACKEND_URL}/api/answers/${token}/`, {
      cache: "no-store",
    });
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}

// ─── Helper Components ────────────────────────────────────────────────────────

function Cb({
  val,
  target = "yes",
}: {
  val: unknown;
  target?: string | boolean | number;
}) {
  const checked = String(val) === String(target);
  if (checked) {
    return (
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          justifyContent: "center",
          width: 13,
          height: 13,
          background: "#1f3864",
          color: "#fff",
          fontSize: 9,
          fontWeight: 900,
          borderRadius: 2,
          lineHeight: "13px",
          border: "1px solid #1f3864",
          flexShrink: 0,
        }}
      >
        ✓
      </span>
    );
  }
  return (
    <span
      style={{
        display: "inline-block",
        width: 13,
        height: 13,
        border: "1.5px solid #8899aa",
        borderRadius: 2,
        background: "#fff",
        flexShrink: 0,
      }}
    />
  );
}

function SecHeader({ title }: { title: string }) {
  return (
    <div
      style={{
        background: "#1f3864",
        color: "#fff",
        padding: "3px 10px",
        fontSize: 8,
        fontWeight: 700,
        letterSpacing: "0.5px",
        textTransform: "uppercase" as const,
      }}
    >
      {title}
    </div>
  );
}

function Ft({ label, text }: { label?: string; text: string }) {
  return (
    <div
      style={{
        padding: "2px 10px 2px 20px",
        borderBottom: "1px solid #dde3ef",
        borderLeft: "3px solid #1f3864",
        background: "#f7f9ff",
        fontSize: 7,
        color: "#444",
        fontStyle: "italic",
      }}
    >
      {label || "Beschreibung"}: {text}
    </div>
  );
}

function YNRow({
  label,
  val,
  ft,
  ftLabel,
  stripe,
  target = "yes",
}: {
  label: string;
  val: unknown;
  ft?: string;
  ftLabel?: string;
  stripe?: boolean;
  target?: string;
}) {
  return (
    <>
      <div
        style={{
          display: "flex",
          alignItems: "flex-start",
          justifyContent: "space-between",
          padding: "3px 10px",
          borderBottom: "1px solid #dde3ef",
          background: stripe ? "#f3f5fa" : "#fff",
          gap: 8,
        }}
      >
        <span style={{ fontSize: 7.5, flex: 1 }}>{label}</span>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 10,
            flexShrink: 0,
          }}
        >
          <span
            style={{
              display: "flex",
              alignItems: "center",
              gap: 3,
              fontSize: 7.5,
            }}
          >
            <Cb val={val} target={target} /> Ja
          </span>
          <span
            style={{
              display: "flex",
              alignItems: "center",
              gap: 3,
              fontSize: 7.5,
            }}
          >
            <Cb val={val} target="no" /> Nein
          </span>
        </div>
      </div>
      {ft && <Ft label={ftLabel} text={ft} />}
    </>
  );
}

function TextRow({
  label,
  value,
  ft,
  ftLabel,
  stripe,
}: {
  label: string;
  value: string;
  ft?: string;
  ftLabel?: string;
  stripe?: boolean;
}) {
  return (
    <>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "3px 10px",
          borderBottom: "1px solid #dde3ef",
          background: stripe ? "#f3f5fa" : "#fff",
          gap: 8,
        }}
      >
        <span style={{ fontSize: 7.5, flex: 1 }}>{label}</span>
        <span
          style={{
            fontSize: 7.5,
            fontWeight: 700,
            color: "#1f3864",
            minWidth: 100,
            textAlign: "right" as const,
          }}
        >
          {value || "—"}
        </span>
      </div>
      {ft && <Ft label={ftLabel} text={ft} />}
    </>
  );
}

function Section({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div
      style={{
        border: "1px solid #c8d0e0",
        borderRadius: 4,
        overflow: "hidden",
        marginBottom: 6,
        breakInside: "avoid" as const,
      }}
    >
      <SecHeader title={title} />
      {children}
    </div>
  );
}

const ESS_LABELS = ESS_QUESTIONS.map((q) => q.text);

function essBandColor(total: number): string {
  return total <= 9 ? "#86efac" : total <= 15 ? "#fdba74" : "#fca5a5";
}

function essBandLabel(total: number): string {
  return total <= 9
    ? `${total}/24 – Normal (0–9)`
    : total <= 15
      ? `${total}/24 – Erhöht (10–15)`
      : `${total}/24 – Ausgeprägt (≥16)`;
}

/** ESS-Tabelle (Kopf, 8 Zeilen, Summenzeile) – Labels konfigurierbar. */
function EssTable({
  labels,
  answers,
  essTotal,
}: {
  labels: string[];
  answers: Record<string, unknown>;
  essTotal: number;
}) {
  return (
    <>
      <div
        style={{
          display: "flex",
          background: "#d8e0ef",
          borderBottom: "1px solid #c8d0e0",
          padding: "2px 10px",
        }}
      >
        <span style={{ flex: 1, fontSize: 7, fontWeight: 700, color: "#1f3864" }}>Situation</span>
        {["0", "1", "2", "3"].map((n) => (
          <span
            key={n}
            style={{
              width: 22,
              textAlign: "center" as const,
              fontSize: 7,
              fontWeight: 700,
              color: "#1f3864",
            }}
          >
            {n}
          </span>
        ))}
      </div>
      {labels.map((label, i) => {
        const val = String(answers[`ess_${i + 1}`] ?? "");
        return (
          <div
            key={i}
            style={{
              display: "flex",
              alignItems: "center",
              padding: "2px 10px",
              borderBottom: "1px solid #dde3ef",
              background: i % 2 === 0 ? "#f3f5fa" : "#fff",
            }}
          >
            <span style={{ flex: 1, fontSize: 6.5, paddingRight: 4 }}>
              {i + 1}. {label}
            </span>
            {[0, 1, 2, 3].map((n) => (
              <span key={n} style={{ width: 22, display: "flex", justifyContent: "center" }}>
                <Cb val={val} target={String(n)} />
              </span>
            ))}
          </div>
        );
      })}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "3px 10px",
          background: "#1f3864",
          color: "#fff",
        }}
      >
        <span style={{ fontSize: 7.5, fontWeight: 700 }}>Gesamtpunktzahl</span>
        <span style={{ fontSize: 8, fontWeight: 900, color: essBandColor(essTotal) }}>
          {essBandLabel(essTotal)}
        </span>
      </div>
    </>
  );
}

/** Kopfbereich mit Titel, Patientendaten, Logo und Arztadresse. */
function PrintHeader({
  data,
  logoDataUrl,
  title,
}: {
  data: AnswerData;
  logoDataUrl: string;
  title: string;
}) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "flex-start",
        border: "1px solid #c8d0e0",
        borderRadius: 4,
        padding: "8px 12px",
        marginBottom: 8,
        background: "#eef1f7",
      }}
    >
      <div style={{ flex: 1 }}>
        <div style={{ fontSize: 14, fontWeight: 900, color: "#1f3864", marginBottom: 5 }}>
          {title}
        </div>
        <table style={{ borderCollapse: "collapse" }}>
          <tbody>
            {([
              ["Name:", data.patient_last_name || "—"],
              ["Vorname:", data.patient_first_name || "—"],
              ["Geburtsdatum:", data.patient_birth_date || "—"],
            ] as [string, string][]).map(([label, value]) => (
              <tr key={label}>
                <td
                  style={{
                    fontSize: 7.5,
                    paddingRight: 8,
                    paddingBottom: 3,
                    color: "#555",
                    width: 80,
                    whiteSpace: "nowrap" as const,
                  }}
                >
                  {label}
                </td>
                <td style={{ fontSize: 7.5, fontWeight: 600, paddingBottom: 3 }}>{value}</td>
              </tr>
            ))}
            <tr>
              <td style={{ fontSize: 7.5, color: "#555" }}>Ausgefüllt am:</td>
              <td style={{ fontSize: 7.5, fontWeight: 700 }}>&nbsp;{data.completed_at || "—"}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div
        style={{
          textAlign: "right" as const,
          fontSize: 7.5,
          lineHeight: 1.7,
          color: "#333",
          display: "flex",
          flexDirection: "column" as const,
          alignItems: "flex-end",
          gap: 4,
        }}
      >
        {/* eslint-disable-next-line @next/next/no-img-element */}
        {logoDataUrl && <img src={logoDataUrl} alt="Logo" style={{ height: 48, width: "auto" }} />}
        <div>
          <div style={{ fontWeight: 700, fontSize: 8.5, color: "#1f3864" }}>Dr. med. Björn Micka</div>
          Betriebsmedizin · Notfallmedizin<br />
          Christoph-Dassler-Str. 22<br />
          91074 Herzogenaurach
        </div>
      </div>
    </div>
  );
}

/** Warnhinweis-§11-Box. */
function WarnBox() {
  return (
    <div
      style={{
        border: "2px solid #1f3864",
        borderRadius: 4,
        padding: "5px 10px",
        background: "#f7f0f0",
        fontSize: 7,
        fontStyle: "italic",
        fontWeight: 700,
        marginBottom: 8,
        lineHeight: 1.5,
        breakInside: "avoid" as const,
      }}
    >
      Zur wahrheitsgemäßen Beantwortung <u>a&nbsp;l&nbsp;l&nbsp;e&nbsp;r</u> Fragen
      sind Sie verpflichtet. Das Verschweigen von Vorerkrankungen stellt einen Verstoß
      gegen §&nbsp;11 FeV dar und kann rechtliche Konsequenzen haben!
    </div>
  );
}

/** Unterschriftenzeilen. */
function SignatureRow() {
  return (
    <div style={{ display: "flex", gap: 16, marginTop: 8, breakInside: "avoid" as const }}>
      {["Ort / Datum", "Unterschrift Patient"].map((label) => (
        <div key={label} style={{ flex: 1 }}>
          <div style={{ borderBottom: "1px solid #555", height: 26, marginBottom: 3 }} />
          <span style={{ fontSize: 7, color: "#555" }}>{label}</span>
        </div>
      ))}
    </div>
  );
}

// ─── V2: generisches Rendering aus dem Schema ─────────────────────────────────

function followupText(
  q: Question,
  answers: Record<string, unknown>
): { ft?: string; ftLabel?: string } {
  const f = q.followup;
  if (!f || answers[q.id] !== (f.when ?? "yes")) return {};
  const raw = answers[f.id];
  if (typeof raw !== "string" || raw.trim() === "") return {};
  return { ft: raw.trim(), ftLabel: f.label };
}

function PrintSection({
  index,
  section,
  answers,
  essTotal,
}: {
  index: number;
  section: SchemaSection;
  answers: Record<string, unknown>;
  essTotal: number;
}) {
  const rows: React.ReactNode[] = [];
  let rowIdx = 0;

  for (const q of section.questions) {
    if (!isVisible(q, answers)) continue;
    const stripe = rowIdx % 2 === 1;

    if (q.type === "ess_matrix") {
      rows.push(
        <div key={q.id}>
          <SecHeader title="ESS – 0 = Nie · 1 = Gering · 2 = Mittel · 3 = Hoch" />
          <EssTable
            labels={(q.items ?? []).map((item) => item.label)}
            answers={answers}
            essTotal={essTotal}
          />
        </div>
      );
      rowIdx = 0;
      continue;
    }

    const { ft, ftLabel } = followupText(q, answers);

    if (q.type === "yes_no") {
      rows.push(
        <YNRow key={q.id} label={q.label} val={answers[q.id]} ft={ft} ftLabel={ftLabel} stripe={stripe} />
      );
    } else if (q.type === "consent") {
      rows.push(
        <YNRow key={q.id} label={q.label} val={String(answers[q.id])} target="true" stripe={stripe} />
      );
    } else {
      // choice / multi_choice / text / textarea
      rows.push(
        <TextRow
          key={q.id}
          label={q.label}
          value={answerDisplay(q, answers[q.id])}
          ft={ft}
          ftLabel={ftLabel}
          stripe={stripe}
        />
      );
    }
    rowIdx++;
  }

  return (
    <Section title={`${index}. ${section.title}`}>
      {rows}
      {section.pdf_note && (
        <div
          style={{
            padding: "3px 10px",
            fontSize: 6.5,
            fontStyle: "italic",
            color: "#444",
            background: "#f7f9ff",
          }}
        >
          {section.pdf_note}
        </div>
      )}
    </Section>
  );
}

function PrintV2({
  data,
  schema,
  logoDataUrl,
}: {
  data: AnswerData;
  schema: Schema;
  logoDataUrl: string;
}) {
  const a = data.answers;
  return (
    <div style={{ padding: "12px", maxWidth: "794px", margin: "0 auto" }}>
      <PrintHeader
        data={data}
        logoDataUrl={logoDataUrl}
        title={schema.title || "Verkehrsmedizinischer Fragebogen"}
      />

      {/* Sektionen in 2 Spalten (CSS columns) */}
      <div style={{ columns: 2, columnGap: 6 }}>
        {schema.sections.map((section, i) => (
          <PrintSection
            key={section.id}
            index={i + 1}
            section={section}
            answers={a}
            essTotal={data.ess_total}
          />
        ))}
      </div>

      <WarnBox />
      <SignatureRow />
    </div>
  );
}

// ─── Legacy (v1-Vorlagen): bisheriges hartkodiertes Layout ────────────────────

function LegacyPrint({ data, logoDataUrl }: { data: AnswerData; logoDataUrl: string }) {
  const a = data.answers;
  const s = (key: string) => String(a[key] ?? "");
  const ft = (key: string) => {
    const v = String(a[key] ?? "").trim();
    return v && !["yes", "no", "none", ""].includes(v) ? v : undefined;
  };

  const alc: Record<string, string> = {
    none: "Keinen", occasional: "Gelegentlich",
    regular: "Regelmäßig", risky: "Riskant",
  };
  const dtMap: Record<string, string> = {
    none: "Kein Diabetes", type1: "Typ 1", type2: "Typ 2",
  };
  const thMap: Record<string, string> = {
    insulin: "Insulin", tablets: "Tabletten", diet: "Diät", other: "Sonstige",
  };

  const hasDm = !["none", "", undefined, null].includes(a.diabetes_type as string);

  return (
    <div style={{ padding: "12px", maxWidth: "794px", margin: "0 auto" }}>

      {/* ══ SEITE 1 ══ */}

      <PrintHeader data={data} logoDataUrl={logoDataUrl} title="Verkehrsmedizinischer Fragebogen" />

      {/* Two-Column Grid */}
      <div style={{ display: "flex", gap: 6 }}>

        {/* ── Left ── */}
        <div style={{ flex: 1, minWidth: 0 }}>

          <Section title="1. Fahrprofil">
            <TextRow label="Führerscheinklassen" value={s("license_classes")} />
            <TextRow label="Fahrzeit pro Tag (h)" value={s("driving_hours")} stripe />
            <YNRow label="Regelmäßige Nachtfahrten" val={a.night_driving} />
            <YNRow label="Unfälle oder Beinahe-Unfälle (24 Monate)" val={a.accidents}
              ft={ft("accidents_desc")} ftLabel="Beschreibung" stripe />
          </Section>

          <Section title="2. Warnsymptome">
            <YNRow label="Ohnmacht oder Bewusstlosigkeit (letzte 5 Jahre)" val={a.syncope} />
            <YNRow label="Krampfanfälle oder epileptische Anfälle" val={a.seizures} stripe />
            <YNRow label="Schwindelattacken" val={a.dizziness} />
            <YNRow label="Neurologische Ausfälle (Lähmung, Sprachstörung)" val={a.neuro_deficit} stripe />
          </Section>

          <Section title="3. Sehen & Hören">
            <YNRow label="Brille oder Kontaktlinsen" val={a.glasses} />
            <YNRow label="Sehprobleme (Doppeltsehen, Gesichtsfeld, Nachtsehen)" val={a.vision_problems}
              ft={ft("vision_desc")} ftLabel="Art der Sehprobleme" stripe />
            <YNRow label="Hörgerät oder relevante Hörstörung" val={a.hearing_aid} />
          </Section>

        </div>

        {/* ── Right ── */}
        <div style={{ flex: 1, minWidth: 0 }}>

          <Section title="4. Herz-Kreislauf">
            <YNRow label="Herzinfarkt oder koronare Erkrankung" val={a.heart_attack} />
            <YNRow label="Rhythmusstörungen, Schrittmacher oder ICD" val={a.arrhythmia} stripe />
            <YNRow label="Herzinsuffizienz" val={a.heart_failure} />
            <YNRow label="Synkopenabklärung bereits erfolgt" val={a.syncope_workup} stripe />
          </Section>

          <Section title="5. Neurologie">
            <YNRow label="Epilepsie" val={a.epilepsy} />
            <YNRow label="Parkinson" val={a.parkinson} stripe />
            <YNRow label="Multiple Sklerose (MS)" val={a.ms} />
            <YNRow label="Migräne mit Aura" val={a.migraine_aura} stripe />
            <YNRow label="Gleichgewichtsstörungen" val={a.balance_disorder} />
          </Section>

        </div>
      </div>

      {/* ══ PAGE BREAK ══ */}
      <div className="page-break" style={{ pageBreakBefore: "always", breakBefore: "page", height: 0 }} />

      {/* ══ SEITE 2 ══ */}

      {/* Page-2 header bar */}
      <div style={{
        background: "#eef1f7", border: "1px solid #c8d0e0", borderRadius: 4,
        padding: "4px 12px", marginBottom: 8,
        display: "flex", justifyContent: "space-between", alignItems: "center",
      }}>
        <span style={{ fontSize: 11, fontWeight: 900, color: "#1f3864" }}>
          Verkehrsmedizinischer Fragebogen – Seite 2
        </span>
        <span style={{ fontSize: 7.5, color: "#555" }}>
          {data.completed_at || "—"}
        </span>
      </div>

      <div style={{ display: "flex", gap: 6 }}>

        {/* ── Left p2 ── */}
        <div style={{ flex: 1, minWidth: 0 }}>

          <Section title="6. Diabetes / Stoffwechsel">
            <TextRow label="Diabetesform" value={dtMap[s("diabetes_type")] || "—"} />
            <YNRow label="Hypoglykämie mit Fremdhilfe (letzte 12 Monate)" val={a.hypoglycemia} stripe />
            {hasDm && <>
              <YNRow label="Hypowahrnehmungsstörung" val={a.hypo_awareness} />
              <TextRow label="Aktuelle Therapie" value={thMap[s("diabetes_therapy")] || "—"} stripe />
            </>}
          </Section>

          <Section title="7. Schlaf & Tagesschläfrigkeit">
            <YNRow label="Ausgeprägte Tagesmüdigkeit" val={a.daytime_sleepiness} />
            <YNRow label="Sekundenschlaf beim Fahren" val={a.microsleep} stripe />
            <YNRow label="Schnarchen oder Atemaussetzer" val={a.snoring} />
          </Section>

          {/* ESS */}
          <div style={{ border: "1px solid #c8d0e0", borderRadius: 4, overflow: "hidden", marginBottom: 6 }}>
            <SecHeader title="ESS – 0 = Nie · 1 = Gering · 2 = Mittel · 3 = Hoch" />
            <EssTable labels={ESS_LABELS} answers={a} essTotal={data.ess_total} />
          </div>

        </div>

        {/* ── Right p2 ── */}
        <div style={{ flex: 1, minWidth: 0 }}>

          <Section title="8. Psychische Gesundheit">
            <YNRow label="Depression, Angststörung oder andere psychiatrische Erkrankung"
              val={a.psychiatric} ft={ft("psychiatric_desc")} ftLabel="Art der Erkrankung" />
            <YNRow label="Stationäre psych. Behandlung in den letzten 5 Jahren"
              val={a.psychiatric_inpatient} stripe />
            <YNRow label="Konzentrations- oder Gedächtnisprobleme" val={a.concentration} />
          </Section>

          <Section title="9. Substanzen & Medikamente">
            <TextRow label="Alkohol" value={alc[s("alcohol")] || "—"} />
            <YNRow label="Drogenkonsum aktuell oder früher" val={a.drugs}
              ft={ft("drugs_desc")} ftLabel="Art und Zeitraum" stripe />
            <YNRow label="Medikamente mit sedierender Wirkung" val={a.sedating_meds}
              ft={ft("sedating_meds_desc")} ftLabel="Welche Medikamente" />
            <YNRow label="Nebenwirkungen wie Schläfrigkeit oder Schwindel" val={a.side_effects} stripe />
          </Section>

          <Section title="10. Einwilligung & Datenschutz">
            <YNRow label="Angaben vollständig und wahrheitsgemäß bestätigt"
              val={String(a.consent_truth)} target="true" />
            <YNRow label="Datenschutzhinweise gelesen und Einwilligung erteilt"
              val={String(a.consent_privacy)} target="true" stripe />
          </Section>

          <WarnBox />
          <SignatureRow />

        </div>
      </div>
    </div>
  );
}

// ─── Page Component ───────────────────────────────────────────────────────────

export default async function PrintPage({
  params,
}: {
  params: Promise<{ token: string }>;
}) {
  const { token } = await params;
  const data = await getAnswerData(token);
  if (!data) notFound();

  const logoDataUrl = getLogoDataUrl();

  if (isV2Schema(data.schema)) {
    return <PrintV2 data={data} schema={data.schema} logoDataUrl={logoDataUrl} />;
  }
  return <LegacyPrint data={data} logoDataUrl={logoDataUrl} />;
}
