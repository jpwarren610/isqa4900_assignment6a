from rest_framework import serializers
from .models import Cook


class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = ('pk', 'event_name', 'event_location', 'year', 'meat', 'injection', 'rub', 'pit', 'fuel', 'pit_temp', 'cook_time', 'final_temp', 'judge_score', 'notes')
