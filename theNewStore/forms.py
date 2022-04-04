from django import forms
from django.forms import Textarea, widgets
from .models import WordModel


class WordForm(forms.ModelForm):
    definition = forms.fields.CharField(max_length=500, widget=Textarea)
    example = forms.fields.CharField(max_length=500, widget=Textarea)
    # ! IMPORTANT NOTE 
    # In meta class you can just contaol over the model fields
    class Meta:
        model = WordModel
        fields = '__all__'
        widgets ={
            'word_type': forms.RadioSelect,
            'audio_file': forms.FileInput(attrs={'accept': 'audio/*'})
        }
    field_order = ['word_text', 'word_type', 'definition', 'example', 'audio_file', 'word_image']

        
