from django import forms

class UploadForm(forms.Form):
    song = forms.CharField(label='Song text', widget=forms.Textarea)
    speech = forms.CharField(label='Speech filepath')

class ConvertForm(forms.Form):
    pass