from django import forms

class SearchForm(forms.Form):
    searchquery = forms.CharField(label='',max_length=100)
