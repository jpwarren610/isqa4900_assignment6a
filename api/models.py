from django.db import models
from django.utils import timezone

# Create your models here.
class Cook(models.Model):
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    year = models.IntegerField(blank=False, null=False)
    meat = models.CharField(max_length=100)
    injection = models.CharField(max_length=100)
    rub = models.CharField(max_length=100)
    pit = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    pit_temp = models.IntegerField(blank=False, null=False)
    cook_time = models.IntegerField(blank=False, null=False)
    final_temp = models.IntegerField(blank=False, null=False)
    judge_score = models.IntegerField(blank=False, null=False)
    notes = models.TextField(max_length=360)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()