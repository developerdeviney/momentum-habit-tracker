from django import forms
from .models import Habit, Daily_Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "habit_name",
            "user",
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Daily_Record
        fields = [
            "date",
            "activity_results",
        ]


class SearchForm(forms.Form):
    habit_name = forms.CharField(max_length=200)