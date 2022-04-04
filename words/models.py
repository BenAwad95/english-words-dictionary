from django.db import models

# Create your models here.


class WordsModel(models.Model):
    word = models.CharField(max_length=50)
    define = models.TextField(blank=False, null=False)
    example = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ['-id']
