from django import forms


class SearchSeriesForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
