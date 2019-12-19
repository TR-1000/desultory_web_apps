from django import forms

class HashForm(forms.Form):
    url = forms.URLField(label='Enter URL here:',required=True)
