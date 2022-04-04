from django.contrib import admin

# Register your models here.
from .models import WordsModel


admin.site.register(WordsModel)
