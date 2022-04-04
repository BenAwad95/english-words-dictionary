from django import urls
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from os.path import splitext
import re


def audio_file_path(instance, filename):
    regex_new_name = re.compile(r"^[\w\d\[\]-_]+")
    new_name = regex_new_name.sub(instance.word_text,filename)
    return "audio/%s"%(new_name)

def image_file_path(instance, filename):
    regex_new_name = re.compile(r"^[\w\d\[\]-_]+")
    new_name = regex_new_name.sub(instance.word_text,filename)
    return "images/%s"%(new_name)

def validate_audio_file(filefiled):
    file_ext = splitext(filefiled.name)[1]
    valid_exts = ['.mp3','.mkv','.pdf']
    if not file_ext in valid_exts:
        raise ValidationError("فضلاً تأكد من الملف")


class WordModel(models.Model):
    word_text = models.CharField(verbose_name='word', max_length=30, unique=True, help_text='Enter new word')
    created_date = models.DateField(verbose_name='createion date', auto_now=True)
    last_modified = models.DateField(verbose_name='last modified', auto_now_add=True)
    VERB = 'v'
    NOUN = 'n'
    ADJECTIVE = 'aj'
    ADVERB = 'av'
    WORD_TYPE_CHOICES = [
        (VERB, 'Verb'),
        (NOUN, 'Noun'),
        (ADJECTIVE, 'Adjective'),
        (ADVERB, 'Adverb')
    ]
    word_type = models.CharField(verbose_name='word type', max_length=10, default= NOUN,choices=WORD_TYPE_CHOICES, blank=False)
    word_image = models.ImageField(verbose_name='an example image', upload_to= image_file_path, blank=True, null=True)
    audio_file = models.FileField(verbose_name='word Pronunciation', upload_to= audio_file_path,max_length=100, blank=True, null=True, validators=[validate_audio_file])
    # audio_sample = models.AudioField()

    # def clean(self):
    #     if not self.audio_file.name.endswith('.mp3'):
    #         raise ValidationError("must be an audio file")
    

    def __str__(self):
        return '%s - %s'%(self.id, self.word_text)

    class Meta:
        ordering = ['-created_date']
    
    def get_absolute_url(self):
        return reverse('theNewStore:word-detail', kwargs={'pk':self.pk})
    
    def update_url(self):
        return reverse('theNewStore:word-update', kwargs={'pk':self.pk})

    def delete_url(self):
        return reverse('theNewStore:word-delete', kwargs={'pk':self.pk})
    
    @property
    def audio_url(self):
        try:
            url = self.audio_file.url
        except: # I will come back and add a exception type
            url = ''
        return url
    
    

class DefinitionsModel(models.Model):
    word = models.ForeignKey(WordModel, verbose_name= 'word' , related_name='definitions', on_delete=models.CASCADE)
    definition_text = models.CharField(verbose_name= 'definition', max_length=500, help_text="word's definition")

    def __str__(self):
        return 'Definition of %s'% self.word.word_text

class ExampleModel(models.Model):
    word = models.ForeignKey(WordModel, verbose_name= 'word' , on_delete=models.CASCADE, related_name='examples')
    example_text = models.CharField(verbose_name= 'example', max_length=500, help_text="word's example")

    def __str__(self):
        return f"Example of {self.word.word_text}" 