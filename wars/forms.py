from django import forms
from .models import War, Battle

class WarForm(forms.ModelForm):

    class Meta:
        model = War
        fields = ('name', 'major_players','key_technologies', 'winner', 'start_date', 'end_date',)

class BattleForm(forms.ModelForm):

    class Meta:
        model = Battle
        fields = ('war', 'name', 'location', 'major_players','key_technologies', 'winner')
