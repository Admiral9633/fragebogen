/**
 * Länder für die Sprachauswahl des Patienten-Fragebogens.
 * `name` = Eigenbezeichnung (Patienten finden ihr Land in der eigenen Sprache),
 * `nameDe` = deutscher Name (Suche durch Praxispersonal), `lang` = Sprachdatei.
 */
export interface Country {
  /** ISO-3166-1 alpha-2 (Kosovo: XK) – zugleich Flaggen-Code */
  code: string;
  name: string;
  nameDe: string;
  lang: string;
}

export const COUNTRIES: Country[] = [
  // ── Mittel-/Westeuropa ────────────────────────────────────────────────────
  { code: "de", name: "Deutschland", nameDe: "Deutschland", lang: "de" },
  { code: "at", name: "Österreich", nameDe: "Österreich", lang: "de" },
  { code: "ch", name: "Schweiz", nameDe: "Schweiz", lang: "de" },
  { code: "gb", name: "United Kingdom", nameDe: "Großbritannien (England)", lang: "en" },
  { code: "ie", name: "Ireland", nameDe: "Irland", lang: "en" },
  { code: "fr", name: "France", nameDe: "Frankreich", lang: "fr" },
  { code: "it", name: "Italia", nameDe: "Italien", lang: "it" },
  { code: "es", name: "España", nameDe: "Spanien", lang: "es" },
  { code: "pt", name: "Portugal", nameDe: "Portugal", lang: "pt" },
  { code: "nl", name: "Nederland", nameDe: "Niederlande", lang: "nl" },
  { code: "be", name: "België", nameDe: "Belgien", lang: "nl" },
  { code: "lu", name: "Luxembourg", nameDe: "Luxemburg", lang: "fr" },
  // ── Nordeuropa ────────────────────────────────────────────────────────────
  { code: "dk", name: "Danmark", nameDe: "Dänemark", lang: "da" },
  { code: "se", name: "Sverige", nameDe: "Schweden", lang: "sv" },
  { code: "no", name: "Norge", nameDe: "Norwegen", lang: "no" },
  { code: "fi", name: "Suomi", nameDe: "Finnland", lang: "fi" },
  { code: "is", name: "Ísland", nameDe: "Island", lang: "is" },
  // ── Mittel-/Osteuropa ─────────────────────────────────────────────────────
  { code: "pl", name: "Polska", nameDe: "Polen", lang: "pl" },
  { code: "cz", name: "Česko", nameDe: "Tschechien", lang: "cs" },
  { code: "sk", name: "Slovensko", nameDe: "Slowakei", lang: "sk" },
  { code: "hu", name: "Magyarország", nameDe: "Ungarn", lang: "hu" },
  { code: "ro", name: "România", nameDe: "Rumänien", lang: "ro" },
  { code: "bg", name: "България", nameDe: "Bulgarien", lang: "bg" },
  { code: "gr", name: "Ελλάδα", nameDe: "Griechenland", lang: "el" },
  { code: "cy", name: "Κύπρος", nameDe: "Zypern", lang: "el" },
  { code: "mt", name: "Malta", nameDe: "Malta", lang: "en" },
  // ── Balkan ────────────────────────────────────────────────────────────────
  { code: "hr", name: "Hrvatska", nameDe: "Kroatien", lang: "hr" },
  { code: "si", name: "Slovenija", nameDe: "Slowenien", lang: "sl" },
  { code: "rs", name: "Srbija", nameDe: "Serbien", lang: "sr" },
  { code: "ba", name: "Bosna i Hercegovina", nameDe: "Bosnien und Herzegowina", lang: "bs" },
  { code: "me", name: "Crna Gora", nameDe: "Montenegro", lang: "sr" },
  { code: "mk", name: "Северна Македонија", nameDe: "Nordmazedonien", lang: "mk" },
  { code: "al", name: "Shqipëria", nameDe: "Albanien", lang: "sq" },
  { code: "xk", name: "Kosova", nameDe: "Kosovo", lang: "sq" },
  { code: "tr", name: "Türkiye", nameDe: "Türkei", lang: "tr" },
  // ── Ehemalige UdSSR ───────────────────────────────────────────────────────
  { code: "ru", name: "Россия", nameDe: "Russland", lang: "ru" },
  { code: "ua", name: "Україна", nameDe: "Ukraine", lang: "uk" },
  { code: "by", name: "Беларусь", nameDe: "Belarus", lang: "be" },
  { code: "md", name: "Moldova", nameDe: "Moldau", lang: "ro" },
  { code: "ge", name: "საქართველო", nameDe: "Georgien", lang: "ka" },
  { code: "am", name: "Հայաստան", nameDe: "Armenien", lang: "hy" },
  { code: "az", name: "Azərbaycan", nameDe: "Aserbaidschan", lang: "az" },
  { code: "kz", name: "Қазақстан", nameDe: "Kasachstan", lang: "kk" },
  { code: "uz", name: "Oʻzbekiston", nameDe: "Usbekistan", lang: "uz" },
  { code: "tm", name: "Türkmenistan", nameDe: "Turkmenistan", lang: "tk" },
  { code: "kg", name: "Кыргызстан", nameDe: "Kirgisistan", lang: "ky" },
  { code: "tj", name: "Тоҷикистон", nameDe: "Tadschikistan", lang: "tg" },
  { code: "lt", name: "Lietuva", nameDe: "Litauen", lang: "lt" },
  { code: "lv", name: "Latvija", nameDe: "Lettland", lang: "lv" },
  { code: "ee", name: "Eesti", nameDe: "Estland", lang: "et" },
  // ── Weitere Herkunftsländer ───────────────────────────────────────────────
  { code: "sy", name: "سوريا", nameDe: "Syrien", lang: "ar" },
  { code: "in", name: "भारत", nameDe: "Indien", lang: "hi" },
  { code: "pk", name: "پاکستان", nameDe: "Pakistan", lang: "ur" },
];

/** Sprachen mit Rechts-nach-links-Schrift */
export const RTL_LANGUAGES = new Set(["ar", "ur"]);
