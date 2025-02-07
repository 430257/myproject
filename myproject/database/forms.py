from django import forms
from django.core.exceptions import ValidationError
from .models import Database


class PageForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = [
            "name",
            "toughness_stats", "power_stats", "muscle_mass_stats",
            "intelligence_stats", "resistance_stats", "speed_stats",
            "toughness_sense", "power_sense", "muscle_mass_sense",
            "intelligence_sense", "resistance_sense", "speed_sense",
            "toughness_effort_value", "power_effort_value", "muscle_mass_effort_value",
            "intelligence_effort_value", "resistance_effort_value", "speed_effort_value"
        ]

    def clean(self):
        cleaned_data = super().clean()

        # **基礎値 (stats) のバリデーション**
        stats_fields = [
            "toughness_stats", "power_stats", "muscle_mass_stats",
            "intelligence_stats", "resistance_stats", "speed_stats"
        ]
        total_stats = sum(cleaned_data.get(field, 0) for field in stats_fields)

        if total_stats > 600:
            self.add_error(None, "基礎値の合計が600を超えています。再度入力してください。")

        for field in stats_fields:
            value = cleaned_data.get(field, 0)
            if value is None or not (0 <= value <= 595):
                self.add_error(field, "基礎値の値は0から595の範囲で入力してください。")

        # **才能 (sense) のバリデーション**
        sense_fields = [
            "toughness_sense", "power_sense", "muscle_mass_sense",
            "intelligence_sense", "resistance_sense", "speed_sense"
        ]

        for field in sense_fields:
            value = cleaned_data.get(field, 0)
            if value is None or not (0 <= value <= 31):
                self.add_error(field, "才能の値は0から31の範囲で入力してください。")

        # **努力値 (effort_value) のバリデーション**
        effort_fields = [
            "toughness_effort_value", "power_effort_value", "muscle_mass_effort_value",
            "intelligence_effort_value", "resistance_effort_value", "speed_effort_value"
        ]
        total_effort = sum(cleaned_data.get(field, 0) for field in effort_fields)

        if total_effort > 512:
            self.add_error(None, "努力値の合計が512を超えています。再度入力してください。")

        for field in effort_fields:
            value = cleaned_data.get(field, 0)
            if value is None or not (0 <= value <= 252):
                self.add_error(field, "努力値の値は0から252の範囲で入力してください。")

        return cleaned_data
