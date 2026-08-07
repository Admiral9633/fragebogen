/**
 * TypeScript-Typen und Helfer für das schema-getriebene Fragebogen-Format
 * (Format-Version 2). Spiegel von backend/questionnaires/schema.py.
 */

export type QuestionType =
  | "yes_no"
  | "choice"
  | "multi_choice"
  | "text"
  | "textarea"
  | "ess_matrix"
  | "consent";

export interface QuestionOption {
  value: string;
  label: string;
}

export interface Followup {
  id: string;
  type: "text" | "textarea";
  label: string;
  /** Antwortwert der Elternfrage, bei dem das Detailfeld erscheint (Default "yes") */
  when?: string;
  required?: boolean;
}

export type ShowIf =
  | { id: string; in: unknown[]; not_in?: never }
  | { id: string; not_in: unknown[]; in?: never };

export interface EssItem {
  id: string;
  label: string;
}

export interface Question {
  id: string;
  type: QuestionType;
  label: string;
  hint?: string;
  required?: boolean;
  error?: string;
  options?: QuestionOption[];
  followup?: Followup;
  show_if?: ShowIf;
  /** Nur ess_matrix: die 8 ESS-Zeilen (ess_1..ess_8) */
  items?: EssItem[];
}

export interface Section {
  id: string;
  title: string;
  subtitle?: string;
  questions: Question[];
  pdf_note?: string;
}

export interface Schema {
  version: number;
  title?: string;
  basis?: string;
  sections: Section[];
}

export type Answers = Record<string, unknown>;

/** True, wenn das Schema das strukturierte v2-Format hat (sections als Objekte). */
export function isV2Schema(schema: unknown): schema is Schema {
  if (!schema || typeof schema !== "object") return false;
  const sections = (schema as { sections?: unknown }).sections;
  return (
    Array.isArray(sections) &&
    sections.length > 0 &&
    typeof sections[0] === "object" &&
    sections[0] !== null
  );
}

/**
 * Wertet show_if gegen die gegebenen Antworten aus
 * (exakt wie backend/questionnaires/schema.py::is_visible).
 */
export function isVisible(question: Question, answers: Answers): boolean {
  const cond = question.show_if;
  if (!cond) return true;
  const value = answers[cond.id];
  if ("in" in cond && cond.in) {
    return cond.in.includes(value as never);
  }
  if ("not_in" in cond && cond.not_in) {
    // Nur sichtbar, wenn eine Antwort vorhanden ist UND sie nicht in der Liste steht
    return value !== undefined && value !== null && !cond.not_in.includes(value as never);
  }
  return true;
}

/** Alle aktuell sichtbaren Fragen einer Sektion. */
export function visibleQuestions(section: Section, answers: Answers): Question[] {
  return section.questions.filter((q) => isVisible(q, answers));
}

/**
 * Antwortwert → Anzeigetext (für Print/PDF), analog
 * backend/questionnaires/schema.py::answer_display.
 */
export function answerDisplay(question: Question, value: unknown): string {
  if (value === null || value === undefined || value === "") return "—";
  const qtype = question.type;
  if (qtype === "yes_no") {
    return value === "yes" ? "Ja" : value === "no" ? "Nein" : "—";
  }
  if (qtype === "consent") {
    return value === true ? "Ja" : "Nein";
  }
  if (qtype === "choice") {
    const opt = (question.options ?? []).find((o) => o.value === value);
    return opt ? opt.label : String(value);
  }
  if (qtype === "multi_choice" && Array.isArray(value)) {
    const byValue = new Map((question.options ?? []).map((o) => [o.value, o.label]));
    const labels = value.map((v) => byValue.get(v as string) ?? String(v));
    return labels.length > 0 ? labels.join(", ") : "—";
  }
  return String(value);
}
