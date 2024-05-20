from django import forms
from .models import Prayer

class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ('name', 'prayer_request')