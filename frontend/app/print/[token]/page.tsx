import { notFound } from "next/navigation";
import fs from "fs";
import path from "path";

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
      {ft && (
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
          {ftLabel || "Beschreibung"}: {ft}
        </div>
      )}
    </>
  );
}

function TextRow({
  label,
  value,
  stripe,
}: {
  label: string;
  value: string;
  stripe?: boolean;
}) {
  return (
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
      }}
    >
      <SecHeader title={title} />
      {children}
    </div>
  );
}

const ESS_LABELS = [
  "Beim Sitzen und Lesen",
  "Beim Fernsehen",
  "Wenn Sie passiv in der Öffentlichkeit sitzen (z.B. im Theater oder bei einer Besprechung)",
  "Als Beifahrer im Auto während einer einstündigen Fahrt ohne Pause",
  "Wenn Sie sich am Nachmittag hingelegt haben, um auszuruhen",
  "Wenn Sie sitzen und sich mit jemandem unterhalten",
  "Wenn Sie nach dem Mittagessen (ohne Alkohol) ruhig dasitzen",
  "Wenn Sie als Fahrer eines Autos verkehrsbedingt einige Minuten halten müssen",
];

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

  const essBandColor =
    data.ess_total <= 9 ? "#86efac" :
    data.ess_total <= 15 ? "#fdba74" : "#fca5a5";
  const essBandLabel =
    data.ess_total <= 9 ? `${data.ess_total}/24 – Normal (0–9)` :
    data.ess_total <= 15 ? `${data.ess_total}/24 – Erhöht (10–15)` :
    `${data.ess_total}/24 – Ausgeprägt (≥16)`;

  return (
    <div style={{ padding: "12px", maxWidth: "794px", margin: "0 auto" }}>

      {/* ══ SEITE 1 ══ */}

      {/* Header */}
      <div style={{
        display: "flex", justifyContent: "space-between", alignItems: "flex-start",
        border: "1px solid #c8d0e0", borderRadius: 4, padding: "8px 12px",
        marginBottom: 8, background: "#eef1f7",
      }}>
        <div style={{ flex: 1 }}>
          <div style={{ fontSize: 14, fontWeight: 900, color: "#1f3864", marginBottom: 5 }}>
            Verkehrsmedizinischer Fragebogen
          </div>
          <table style={{ borderCollapse: "collapse" }}>
            <tbody>
              {([
                ["Name:", data.patient_last_name || "—"],
                ["Vorname:", data.patient_first_name || "—"],
                ["Geburtsdatum:", data.patient_birth_date || "—"],
              ] as [string, string][]).map(([label, value]) => (
                <tr key={label}>
                  <td style={{ fontSize: 7.5, paddingRight: 8, paddingBottom: 3, color: "#555", width: 80, whiteSpace: "nowrap" as const }}>
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
        <div style={{ textAlign: "right" as const, fontSize: 7.5, lineHeight: 1.7, color: "#333", display: "flex", flexDirection: "column" as const, alignItems: "flex-end", gap: 4 }}>
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
            <div style={{
              display: "flex", background: "#d8e0ef",
              borderBottom: "1px solid #c8d0e0", padding: "2px 10px",
            }}>
              <span style={{ flex: 1, fontSize: 7, fontWeight: 700, color: "#1f3864" }}>Situation</span>
              {["0","1","2","3"].map(n => (
                <span key={n} style={{ width: 22, textAlign: "center" as const, fontSize: 7, fontWeight: 700, color: "#1f3864" }}>
                  {n}
                </span>
              ))}
            </div>
            {ESS_LABELS.map((label, i) => {
              const val = String(a[`ess_${i + 1}`] ?? "");
              return (
                <div key={i} style={{
                  display: "flex", alignItems: "center",
                  padding: "2px 10px", borderBottom: "1px solid #dde3ef",
                  background: i % 2 === 0 ? "#f3f5fa" : "#fff",
                }}>
                  <span style={{ flex: 1, fontSize: 6.5, paddingRight: 4 }}>{i + 1}. {label}</span>
                  {[0,1,2,3].map(n => (
                    <span key={n} style={{ width: 22, display: "flex", justifyContent: "center" }}>
                      <Cb val={val} target={String(n)} />
                    </span>
                  ))}
                </div>
              );
            })}
            <div style={{
              display: "flex", alignItems: "center", justifyContent: "space-between",
              padding: "3px 10px", background: "#1f3864", color: "#fff",
            }}>
              <span style={{ fontSize: 7.5, fontWeight: 700 }}>Gesamtpunktzahl</span>
              <span style={{ fontSize: 8, fontWeight: 900, color: essBandColor }}>{essBandLabel}</span>
            </div>
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

          {/* Warnhinweis */}
          <div style={{
            border: "2px solid #1f3864", borderRadius: 4, padding: "5px 10px",
            background: "#f7f0f0", fontSize: 7, fontStyle: "italic",
            fontWeight: 700, marginBottom: 8, lineHeight: 1.5,
          }}>
            Zur wahrheitsgemäßen Beantwortung <u>a&nbsp;l&nbsp;l&nbsp;e&nbsp;r</u> Fragen
            sind Sie verpflichtet. Das Verschweigen von Vorerkrankungen stellt einen Verstoß
            gegen §&nbsp;11 FeV dar und kann rechtliche Konsequenzen haben!
          </div>

          {/* Unterschrift */}
          <div style={{ display: "flex", gap: 16, marginTop: 8 }}>
            {["Ort / Datum", "Unterschrift Patient"].map(label => (
              <div key={label} style={{ flex: 1 }}>
                <div style={{ borderBottom: "1px solid #555", height: 26, marginBottom: 3 }} />
                <span style={{ fontSize: 7, color: "#555" }}>{label}</span>
              </div>
            ))}
          </div>

        </div>
      </div>
    </div>
  );
}

