/**
 * ESS (Epworth Sleepiness Scale) Berechnungs-Logik
 */

export const ESS_IDS = [
  "ess_1",
  "ess_2",
  "ess_3",
  "ess_4",
  "ess_5",
  "ess_6",
  "ess_7",
  "ess_8",
] as const;

export type ESSId = typeof ESS_IDS[number];

export interface ESSResult {
  total: number;
  band: "normal" | "erhöht" | "ausgeprägt";
  bandLabel: string;
  bandColor: string;
}

export function calcESS(values: Record<string, any>): ESSResult {
  const total = ESS_IDS.reduce((sum, id) => {
    return sum + Number(values[id] ?? 0);
  }, 0);

  let band: "normal" | "erhöht" | "ausgeprägt";
  let bandLabel: string;
  let bandColor: string;

  if (total >= 16) {
    band = "ausgeprägt";
    bandLabel = "Ausgeprägt (≥16)";
    bandColor = "text-red-600";
  } else if (total >= 10) {
    band = "erhöht";
    bandLabel = "Erhöht (10-15)";
    bandColor = "text-orange-600";
  } else {
    band = "normal";
    bandLabel = "Normal (0-9)";
    bandColor = "text-green-600";
  }

  return { total, band, bandLabel, bandColor };
}

export const ESS_QUESTIONS = [
  {
    id: "ess_1" as const,
    text: "Beim Sitzen und Lesen",
  },
  {
    id: "ess_2" as const,
    text: "Beim Fernsehen",
  },
  {
    id: "ess_3" as const,
    text: "Wenn Sie passiv in der Öffentlichkeit sitzen (z.B. im Theater oder bei einer Besprechung)",
  },
  {
    id: "ess_4" as const,
    text: "Als Beifahrer im Auto während einer einstündigen Fahrt ohne Pause",
  },
  {
    id: "ess_5" as const,
    text: "Wenn Sie sich am Nachmittag hingelegt haben, um auszuruhen",
  },
  {
    id: "ess_6" as const,
    text: "Wenn Sie sitzen und sich mit jemandem unterhalten",
  },
  {
    id: "ess_7" as const,
    text: "Wenn Sie nach dem Mittagessen (ohne Alkohol) ruhig dasitzen",
  },
  {
    id: "ess_8" as const,
    text: "Wenn Sie als Fahrer eines Autos verkehrsbedingt einige Minuten halten müssen",
  },
];

export const ESS_OPTIONS = [
  { value: "0", label: "0 - Würde nie einnicken" },
  { value: "1", label: "1 - Geringe Wahrscheinlichkeit" },
  { value: "2", label: "2 - Mittlere Wahrscheinlichkeit" },
  { value: "3", label: "3 - Hohe Wahrscheinlichkeit" },
];
