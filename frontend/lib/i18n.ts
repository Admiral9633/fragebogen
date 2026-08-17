/**
 * Übersetzungen für den Patienten-Fragebogen.
 *
 * Der Katalog (Schema) bleibt deutsch und kanonisch; eine Sprachdatei vom
 * Backend (/api/i18n/<lang>/) übersetzt ausschließlich die Anzeige-Texte.
 * Antworten werden als sprachunabhängige Werte gespeichert — PDF und
 * Auswertung für die Praxis bleiben deutsch.
 */
import type { Question, Schema } from "@/lib/schema";

export interface Translation {
  _meta: { language: string; name: string; machine_translated?: boolean };
  ui: Record<string, string>;
  sections: Record<string, { title: string; subtitle: string }>;
  questions: Record<
    string,
    {
      label: string;
      hint?: string;
      error?: string;
      options?: Record<string, string>;
      followup?: string;
    }
  >;
  ess_items: Record<string, string>;
}

/** Deutsche UI-Texte als Fallback (identisch zum Backend-Master). */
export const UI_DE: Record<string, string> = {
  header_title: "Verkehrsmedizinischer Fragebogen",
  header_subtitle: "Bitte beantworten Sie alle Fragen",
  language_label: "Sprache",
  loading: "Lade Fragebogen …",
  not_found_title: "Fragebogen nicht gefunden",
  to_start: "Zur Startseite",
  back: "Zurück",
  next: "Weiter",
  skip: "Überspringen",
  submit: "Absenden",
  sending: "Senden…",
  question_of: "Frage {current} von {total}",
  answer_placeholder: "Ihre Antwort…",
  required_error: "Bitte beantworten Sie diese Frage.",
  yes: "Ja",
  no: "Nein",
  consent_title: "Einwilligung",
  followup_hint: "Freiwillige Zusatzangabe – hilft bei der ärztlichen Beurteilung.",
  ess_question: "Wie wahrscheinlich ist es, dass Sie in dieser Situation einnicken würden?",
  ess_sum: "Bisherige Summe",
  ess_opt_0: "0 – Würde nie einnicken",
  ess_opt_1: "1 – Geringe Wahrscheinlichkeit",
  ess_opt_2: "2 – Mittlere Wahrscheinlichkeit",
  ess_opt_3: "3 – Hohe Wahrscheinlichkeit",
  privacy_button: "Datenschutzhinweise anzeigen",
  privacy_title: "Datenschutzhinweise",
  privacy_subtitle: "Information zur Verarbeitung Ihrer Daten nach Art. 13 DSGVO",
  privacy_controller:
    "Verantwortlicher: Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach",
  privacy_purpose:
    "Zweck der Verarbeitung: Ihre Angaben in diesem Fragebogen (einschließlich Gesundheitsdaten) werden ausschließlich zur Vorbereitung und Durchführung Ihrer verkehrsmedizinischen Untersuchung verwendet.",
  privacy_legal:
    "Rechtsgrundlage: Ihre Einwilligung (Art. 6 Abs. 1 lit. a, Art. 9 Abs. 2 lit. a DSGVO). Sie können die Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen.",
  privacy_storage:
    "Speicherung: Das Ergebnis wird in Ihre Untersuchungsunterlagen übernommen und unterliegt den ärztlichen Aufbewahrungsfristen. Der Online-Zugang über Ihren persönlichen Link erlischt nach Ablauf der Gültigkeit; die Daten dieses Online-Fragebogens werden anschließend routinemäßig gelöscht.",
  privacy_rights:
    "Ihre Rechte: Sie haben das Recht auf Auskunft, Berichtigung, Löschung und Einschränkung der Verarbeitung sowie ein Beschwerderecht bei der zuständigen Datenschutz-Aufsichtsbehörde.",
  privacy_secrecy: "Alle Angaben unterliegen der ärztlichen Schweigepflicht.",
  success_title: "Vielen Dank!",
  success_text: "Ihr Fragebogen wurde erfolgreich übermittelt.",
  success_result: "ESS-Ergebnis",
  success_doctor_note:
    "Bitte besprechen Sie das Ergebnis mit Ihrem Arzt. Eine abschließende Bewertung erfolgt durch einen Facharzt.",
  success_pdf: "PDF-Zusammenfassung herunterladen",
  success_close: "Sie können dieses Fenster nun schließen.",
  band_normal: "Normal (0–9)",
  band_elevated: "Erhöht (10–15)",
  band_severe: "Ausgeprägt (≥16)",
  submit_error: "Fehler beim Absenden. Bitte prüfen Sie Ihre Angaben.",
};

export type UiStrings = typeof UI_DE;

/** UI-Texte einer Übersetzung mit deutschem Fallback. */
export function uiStrings(translation: Translation | null): UiStrings {
  if (!translation) return UI_DE;
  return { ...UI_DE, ...translation.ui };
}

/** Sprachdatei vom Backend holen (null bei "de" oder Fehler → deutscher Katalog). */
export async function fetchTranslation(lang: string): Promise<Translation | null> {
  if (!lang || lang === "de") return null;
  try {
    const res = await fetch(`/api/i18n/${lang}/`);
    if (!res.ok) return null;
    return (await res.json()) as Translation;
  } catch {
    return null;
  }
}

function translateQuestion(q: Question, t: Translation): Question {
  if (q.type === "ess_matrix") {
    return {
      ...q,
      hint: t.ui.ess_question ?? q.hint,
      items: (q.items ?? []).map((item) => ({
        ...item,
        label: t.ess_items[item.id] ?? item.label,
      })),
    };
  }
  const tq = t.questions[q.id];
  if (!tq) return q;
  return {
    ...q,
    label: tq.label || q.label,
    hint: tq.hint ?? q.hint,
    error: tq.error ?? q.error,
    options: q.options?.map((o) => ({
      ...o,
      label: tq.options?.[o.value] || o.label,
    })),
    followup: q.followup
      ? { ...q.followup, label: tq.followup || q.followup.label }
      : undefined,
  };
}

/** Schema mit übersetzten Anzeige-Texten (Struktur/IDs/Values unverändert). */
export function translateSchema(schema: Schema, translation: Translation | null): Schema {
  if (!translation) return schema;
  return {
    ...schema,
    sections: schema.sections.map((section) => ({
      ...section,
      title: translation.sections[section.id]?.title || section.title,
      subtitle: translation.sections[section.id]?.subtitle || section.subtitle,
      questions: section.questions.map((q) => translateQuestion(q, translation)),
    })),
  };
}
