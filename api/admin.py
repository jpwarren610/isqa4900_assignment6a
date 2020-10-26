from django.contrib import admin
from .models import Cook

# Register your models here.
class CookList(admin.ModelAdmin):
    list_display = ('event_name', 'event_location', 'year', 'meat', 'injection', 'rub', 'pit', 'fuel', 'pit_temp', 'cook_time', 'final_temp', 'judge_score', 'notes')
    list_filter = ('event_name', 'year', 'meat', 'injection', 'rub', 'pit', 'fuel', 'judge_score')
    search_fields = ('name', 'year', 'meat', 'injection', 'rub', 'pit', 'fuel', 'judge_score')
    ordering = ['year']


admin.site.register(Cook, CookList)
