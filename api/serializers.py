from rest_framework import serializers
from .models import Cook


class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = ('pk', 'event_name', 'event_location', 'year', 'meat', 'weight', 'injection', 'rub', 'mop_sauce', 'pit', 'fuel', 'pit_temp', 'cook_time', 'final_temp', 'personal_score', 'judge_score', 'awared', 'notes')
