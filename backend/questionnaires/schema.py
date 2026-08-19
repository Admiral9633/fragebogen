"""
Schema-getriebener Fragebogen: Hilfsfunktionen für Validierung und Rendering.

Das Schema liegt als schema_json am QuestionnaireTemplate (Format-Version 2):

{
  "version": 2,
  "title": "...",
  "basis": "...",
  "sections": [
    {
      "id": "fahrprofil", "title": "...", "subtitle": "...",
      "questions": [
        {"id": "...", "type": "yes_no|choice|multi_choice|text|textarea|ess_matrix|consent",
         "label": "...", "hint": "...", "required": true,
         "options": [{"value": "...", "label": "..."}],       # choice/multi_choice
         "followup": {"id": "...", "type": "text|textarea", "label": "...",
                       "when": "yes", "required": false},       # optionales Detailfeld
         "show_if": {"id": "andere_frage", "in": [...]} |
                    {"id": "andere_frage", "not_in": [...]}     # bedingte Sichtbarkeit
        }
      ]
    }
  ]
}

Antwortformat (answers_json): {frage_id: wert}. yes_no → "yes"/"no",
choice → Options-value, multi_choice → Liste von values, consent → true,
ess_matrix → ess_1..ess_8 als int 0-3 (direkt auf oberster Ebene).
"""

ESS_KEYS = [f"ess_{i}" for i in range(1, 9)]

MAX_TEXT_LENGTH = 2000


def is_v2_schema(schema):
    """True, wenn schema_json das strukturierte Format (sections als Objekte) hat."""
    sections = (schema or {}).get("sections")
    return bool(sections) and isinstance(sections[0], dict)


def iter_questions(schema):
    """Alle (section, question)-Paare in Dokumentreihenfolge."""
    for section in schema.get("sections", []):
        for question in section.get("questions", []):
            yield section, question


def is_visible(question, answers):
    """Wertet show_if gegen die gegebenen Antworten aus."""
    cond = question.get("show_if")
    if not cond:
        return True
    value = answers.get(cond.get("id"))
    if "in" in cond:
        return value in cond["in"]
    if "not_in" in cond:
        return value is not None and value not in cond["not_in"]
    return True


def _clean_text(value):
    return str(value).strip()[:MAX_TEXT_LENGTH]


def _option_values(question):
    return [o.get("value") for o in question.get("options", [])]


def validate_answers(schema, data):
    """
    Validiert eingereichte Antworten gegen das Schema.

    Returns (cleaned, errors):
      cleaned – Whitelist der bekannten Antworten (inkl. ess_total/ess_band),
      errors  – {frage_id: meldung}; leer bei Erfolg.
    """
    cleaned = {}
    errors = {}

    def require(qid, label):
        errors[qid] = f"„{label}“ ist erforderlich."

    def handle_followup(question):
        follow = question.get("followup")
        if not follow:
            return
        when = follow.get("when", "yes")
        if data.get(question["id"]) != when:
            return
        raw = data.get(follow["id"])
        if raw is None or _clean_text(raw) == "":
            if follow.get("required"):
                require(follow["id"], follow.get("label", follow["id"]))
            return
        cleaned[follow["id"]] = _clean_text(raw)

    for _section, q in iter_questions(schema):
        qid = q["id"]
        qtype = q.get("type")
        label = q.get("label", qid)
        required = bool(q.get("required"))

        if not is_visible(q, data):
            continue

        if qtype == "ess_matrix":
            for key in ESS_KEYS:
                raw = data.get(key)
                try:
                    value = int(raw)
                except (TypeError, ValueError):
                    errors[key] = "Bitte einen Wert von 0 bis 3 auswählen."
                    continue
                if not 0 <= value <= 3:
                    errors[key] = "Bitte einen Wert von 0 bis 3 auswählen."
                    continue
                cleaned[key] = value
            continue

        raw = data.get(qid)

        if qtype == "yes_no":
            if raw in ("yes", "no"):
                cleaned[qid] = raw
                handle_followup(q)
            elif required:
                require(qid, label)

        elif qtype == "choice":
            if raw in _option_values(q):
                cleaned[qid] = raw
                handle_followup(q)
            elif required:
                require(qid, label)

        elif qtype == "multi_choice":
            allowed = set(_option_values(q))
            if isinstance(raw, list):
                values = [v for v in raw if v in allowed]
                if values:
                    cleaned[qid] = values
                elif required:
                    require(qid, label)
            elif required:
                require(qid, label)

        elif qtype in ("text", "textarea"):
            if raw is not None and _clean_text(raw) != "":
                cleaned[qid] = _clean_text(raw)
            elif required:
                require(qid, label)

        elif qtype == "consent":
            if raw is True:
                cleaned[qid] = True
            else:
                errors[qid] = q.get(
                    "error", "Bitte bestätigen Sie diese Erklärung."
                )

    if not errors and all(k in cleaned for k in ESS_KEYS):
        total = sum(cleaned[k] for k in ESS_KEYS)
        cleaned["ess_total"] = total
        cleaned["ess_band"] = ess_band(total)

    return cleaned, errors


def ess_band(total):
    if total >= 16:
        return "ausgeprägt"
    if total >= 10:
        return "erhöht"
    return "normal"


def answer_display(question, value):
    """Antwortwert → Anzeigetext (für PDF/Print)."""
    if value is None or value == "":
        return "—"
    qtype = question.get("type")
    if qtype == "yes_no":
        return {"yes": "Ja", "no": "Nein"}.get(value, "—")
    if qtype == "consent":
        return "Ja" if value is True else "Nein"
    if qtype in ("choice",):
        for opt in question.get("options", []):
            if opt.get("value") == value:
                return opt.get("label", str(value))
        return str(value)
    if qtype == "multi_choice" and isinstance(value, list):
        labels = []
        by_value = {o.get("value"): o.get("label") for o in question.get("options", [])}
        for v in value:
            labels.append(by_value.get(v, str(v)))
        return ", ".join(labels) if labels else "—"
    return str(value)
