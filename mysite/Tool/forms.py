from django import forms

class NameForm(forms.Form):
    Pollutant = forms.CharField(label='Pollutant', max_length=100)
    Concentration = forms.IntField(label='Concentration', max_length=100)

    
