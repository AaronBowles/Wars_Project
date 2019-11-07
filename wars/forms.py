from django import forms
from .model import War

class WarForm(forms.ModelForm):

    class Meta:
        model = War
        fields = ('name', 'major_players','key_technologies', 'winner', 'start_date', 'end_date',)

