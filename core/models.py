from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="habits")
    habit_name = models.CharField(max_length=255)


class Daily_Record(models.Model):
    habit = models.ForeignKey(
        to=Habit, on_delete=models.CASCADE, related_name="daily_records"
    )
    date = models.DateField()
    activity_results = models.IntegerField(null=True)

    class Meta:
        unique_together = [
            "date",
            "habit",
        ]
