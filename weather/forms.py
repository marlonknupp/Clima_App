from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Digite o nome da cidade', max_length=100)