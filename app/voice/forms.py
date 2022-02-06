from django import forms

class UploadForm(forms.Form):
    song = forms.CharField(label='Song text', widget=forms.Textarea)
    speech = forms.CharField(label='Speech filepath')