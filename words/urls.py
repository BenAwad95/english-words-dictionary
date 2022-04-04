from django.urls import path
from .views import wordsList, createWord, wordDetail, updateWord, deleteWord
app_name = 'words'
urlpatterns = [
    path('', wordsList, name='words_list'),
    path('create/', createWord, name='create_word'),
    path('<int:id>/', wordDetail, name='word_detail'),
    path('<int:id>/update', updateWord, name='update_word'),
    path('<int:id>/delete', deleteWord, name='delete_word')
]
