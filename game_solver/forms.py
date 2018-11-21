from django import forms

class NewSudokuForm(forms.Form):
    input = forms.CharField(label="Input:", max_length=81)

