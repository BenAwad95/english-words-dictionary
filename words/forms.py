from django import forms
from .models import WordsModel


class WordsModelForm(forms.ModelForm):
    word = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Word'
    }), required=True)
    define = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': ' Definition'
    }), required=True)
    example = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': ' Example'
    }), required=True)

    class Meta:
        model = WordsModel
        fields = (
            'word',
            'define',
            'example'
        )
