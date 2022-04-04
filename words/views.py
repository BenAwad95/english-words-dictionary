from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import WordsModel
from .forms import WordsModelForm
from random import choice
# Create your views here.


def wordsList(request):
    words_list = WordsModel.objects.all()
    word = choice(words_list)
    # print(word.word)
    context = {
        'words': words_list,
        'random_word': word,
        'page_title': "Words List"
    }

    return render(request, 'words\\wordsList.html', context)

    


def wordDetail(request, id):
    words_list = WordsModel.objects.all()
    word = WordsModel.objects.get(pk=id)
    # print(word.word)
    context = {
        'words': words_list,
        'random_word': word,
        'page_title': word.word
    }

    return render(request, 'words\\wordsList.html', context)

# RAW FORM

# def createWord(request):
#     if request.method == 'POST':
#         word = request.POST.get('word')
#         define = request.POST.get('define')
#         example = request.POST.get('example')
#         WordsModel.objects.create(word=word, define=define, example=example)
#         return wordsList(request)
#     return render(request, 'words\\word_form.html', {'page_title': 'Add Word'})

# DJANGO FORM


def createWord(request):
    form = WordsModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return wordsList(request)
    return render(request, 'words\\word_form.html', {
        'page_title': 'Add Word',
        'form': form
    })


def updateWord(request, id):
    obj = WordsModel.objects.get(pk=id)
    form = WordsModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        # print(form)
        form.save()
        # return redirect('../')
        return wordDetail(request, id)
    return render(request, 'words\\word_form.html', {
        'page_title': 'Update Word',
        'form': form
    })


def deleteWord(request, id):
    obj = get_object_or_404(WordsModel, id=id)
    if request.method == 'POST':
        obj.delete()
        return wordsList(request)
    return render(request, 'words\\word_delete_confirm.html', {
        'page_title': 'Delete word',
        'word': obj
    })
