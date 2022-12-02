"""Forms for bts_info app."""

from django import forms


class BtsIdForm(forms.Form):
    """Present bts id form for requesting site data."""

    bts_id = forms.CharField(
        label='',
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'id': 'input-field',
                'placeholder': 'Enter site id',
                'class': 'form-control',
            },
        ),
    )
