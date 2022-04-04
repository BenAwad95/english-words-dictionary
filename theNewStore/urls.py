from django.urls import path
from .views import WordListView, WordCreateView, WordDetailView, \
    WordUpdateView, WordDeleteView


app_name = 'theNewStore'

urlpatterns = [
    path('', WordListView.as_view(), name='word_list'),
    path('detail/<int:pk>/', WordDetailView.as_view(), name='word-detail'),
    path('create/', WordCreateView.as_view(), name='word_create'),
    path('update/<int:pk>/', WordUpdateView.as_view(), name='word-update'),
    path('delete/<int:pk>/', WordDeleteView.as_view(), name='word-delete'),
]
