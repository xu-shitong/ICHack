from django import forms

class SongForm(forms.Form):
    track = forms.FileField(label='Track')