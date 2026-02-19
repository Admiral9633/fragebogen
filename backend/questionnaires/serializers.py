from rest_framework import serializers
from .models import QuestionnaireTemplate, QuestionnaireSession, AnswerSet


# ESS Konstanten
ESS_KEYS = [f"ess_{i}" for i in range(1, 9)]


def calc_ess_total(data):
    """Berechne ESS Gesamtscore"""
    return sum(int(data.get(k, 0)) for k in ESS_KEYS)


def get_ess_band(total):
    """Bestimme ESS Kategorie basierend auf Score"""
    if total >= 16:
        return "ausgeprägt"
    elif total >= 10:
        return "erhöht"
    else:
        return "normal"


class QuestionnaireTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireTemplate
        fields = ['id', 'slug', 'version', 'schema_json', 'is_active']


class QuestionnaireSessionSerializer(serializers.ModelSerializer):
    template_slug = serializers.CharField(source='template.slug', read_only=True)
    is_valid = serializers.SerializerMethodField()
    
    class Meta:
        model = QuestionnaireSession
        fields = [
            'token', 'template_slug', 'created_at', 
            'expires_at', 'completed', 'is_valid'
        ]
        read_only_fields = ['token', 'created_at']
    
    def get_is_valid(self, obj):
        return obj.is_valid()


class SubmitSerializer(serializers.Serializer):
    """
    Flexibler Serializer für den vollständigen Verkehrsmedizin-Fragebogen.
    Alle Felder außer ESS und Einwilligung werden als optionale Freitext-/Boolean-Felder
    gespeichert und vollständig in answers_json abgelegt.
    """
    # ── ESS Felder (8 Items, jeweils 0-3) ────────────────────────────────────
    ess_1 = serializers.IntegerField(min_value=0, max_value=3)
    ess_2 = serializers.IntegerField(min_value=0, max_value=3)
    ess_3 = serializers.IntegerField(min_value=0, max_value=3)
    ess_4 = serializers.IntegerField(min_value=0, max_value=3)
    ess_5 = serializers.IntegerField(min_value=0, max_value=3)
    ess_6 = serializers.IntegerField(min_value=0, max_value=3)
    ess_7 = serializers.IntegerField(min_value=0, max_value=3)
    ess_8 = serializers.IntegerField(min_value=0, max_value=3)

    # ── Einwilligung (Pflichtfelder) ──────────────────────────────────────────
    consent_truth = serializers.BooleanField(required=True)
    consent_privacy = serializers.BooleanField(required=True)

    # ── Alle weiteren Felder werden über to_internal_value() durchgeleitet ───
    # (keine harte Deklaration nötig – wird flexibel gespeichert)

    def to_internal_value(self, data):
        """Accept all keys; validate only the declared fields strictly."""
        declared_keys = set(self.fields.keys())
        # Run normal validation for declared fields
        validated = super().to_internal_value(
            {k: v for k, v in data.items() if k in declared_keys}
        )
        # Merge all remaining keys (stored verbatim in answers_json)
        for key, value in data.items():
            if key not in declared_keys:
                validated[key] = value
        return validated

    def validate(self, attrs):
        # Berechne ESS Total und Band
        total = calc_ess_total(attrs)
        attrs['ess_total'] = total
        attrs['ess_band'] = get_ess_band(total)

        # Validiere Einwilligungen
        if not attrs.get('consent_truth'):
            raise serializers.ValidationError(
                "Bitte bestätigen Sie die Vollständigkeit Ihrer Angaben."
            )
        if not attrs.get('consent_privacy'):
            raise serializers.ValidationError(
                "Bitte akzeptieren Sie die Datenschutzhinweise."
            )

        return attrs


class AnswerSetSerializer(serializers.ModelSerializer):
    session_token = serializers.UUIDField(source='session.token', read_only=True)
    
    class Meta:
        model = AnswerSet
        fields = [
            'id', 'session_token', 'answers_json', 
            'ess_total', 'ess_band', 'created_at'
        ]
        read_only_fields = ['created_at']
