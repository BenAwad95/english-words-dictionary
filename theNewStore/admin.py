from django.contrib import admin

from .models import WordModel, DefinitionsModel, ExampleModel

admin.site.register(WordModel)
admin.site.register(DefinitionsModel)
admin.site.register(ExampleModel)
