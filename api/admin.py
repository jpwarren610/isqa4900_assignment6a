from django.contrib import admin
from .models import Cook

# Register your models here.
class CookList(admin.ModelAdmin):
    list_display = ('event_name', 'event_location', 'year', 'meat', 'weight', 'injection', 'rub', 'mop_sauce', 'pit', 'fuel', 'pit_temp', 'cook_time', 'final_temp', 'personal_score', 'judge_score', 'award', 'notes')
    list_filter = ('event_name', 'year', 'meat', 'injection', 'rub', 'mop_sauce', 'pit', 'fuel', 'personal_score', 'judge_score')
    search_fields = ('name', 'year', 'meat', 'injection', 'rub', 'mop_sauce', 'pit', 'fuel', 'judge_score')
    ordering = ['year']


admin.site.register(Cook, CookList)
