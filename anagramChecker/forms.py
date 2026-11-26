from django import forms

INPUT_ATTRS = {"class": "input input-bordered w-full", "autocomplete": "off"}


class AnagramForm(forms.Form):
    """Form for entering two words or phrases to check for anagrams."""

    first = forms.CharField(
        label="First word or phrase",
        max_length=200,
        widget=forms.TextInput(attrs={**INPUT_ATTRS, "placeholder": "e.g. listen"}),
    )
    second = forms.CharField(
        label="Second word or phrase",
        max_length=200,
        widget=forms.TextInput(attrs={**INPUT_ATTRS, "placeholder": "e.g. silent"}),
    )
