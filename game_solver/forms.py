from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_sudoku(value):
    if value.isdigit() == False:
        raise ValidationError(
            _('%(value)s contains digits other than 0-9'),
            params={'value': value},
        )
    if len(value) < 81:
        raise ValidationError(
            _('%(value)s is not enough characters to make a sudoku board'),
            params={'value': value},
        )

class NewSudokuForm(forms.Form):
    input = forms.CharField(label="Input:", max_length=81, validators=[validate_sudoku])

