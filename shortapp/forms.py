from django import forms

class LinkForm(forms.Form):
    long_url = forms.URLField(label="Long URL", widget=forms.URLInput(attrs={"class": "form-control"}))
    custom_code = forms.CharField(required=False, min_length=4, max_length=16, widget=forms.TextInput(attrs={"class": "form-control"}))
    days_valid = forms.IntegerField(required=False, min_value=1, max_value=365, widget=forms.NumberInput(attrs={"class": "form-control"}))
