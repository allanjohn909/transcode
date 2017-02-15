from django import forms

class ListForm(forms.Form):
    list_path=forms.CharField(required=True)
    