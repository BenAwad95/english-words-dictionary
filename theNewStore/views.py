#todo  import the view lib
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import WordModel, DefinitionsModel, ExampleModel
from .forms import WordForm
import random
from .utlls import get_link_from_url
# ? import prefetch due to handle the relented objects

app_name = 'theNewStore'

# for word in WordsModel.objects.all():
#     try:
#         word_obj = WordModel(word_text=word.word)
#         word_obj.save()
#         for def_ in word.define.split('-'):
#             defintion = DefinitionsModel(word=word_obj, definition_text=def_)
#             defintion.save()
#         for exa in word.example.split('-'):
#             example = ExampleModel(word=word_obj, example_text=exa)
#             example.save()
#     except:
#         pass


class WordListView(ListView):

    def get_queryset(self):
        # return WordModel.objects.prefetch_related(Prefetch('examples'),Prefetch('definitions'))
        query_set = WordModel.objects.prefetch_related('examples','definitions')
        # query = random.shuffle(list(query_set))
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_word'] = random.choice(WordModel.objects.prefetch_related('examples','definitions'))
        # context['definitions'] = ', '.join(list(map(lambda q: q.definition_text, context['random_word'].definitions.all())))
        # context['examples'] = ', '.join(list(map(lambda q: q.example_text, context['random_word'].examples.all())))
        query_set = list(WordModel.objects.prefetch_related('examples','definitions'))
        random.shuffle(query_set)
        # print(query_set)
        context['object_list'] = query_set[:10]
        context['page_title'] = 'All words'
        return context


class WordDetailView(DetailView):
    model = WordModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # word_obj = self.get_object()
        # context['definitions'] = ' - '.join(list(map(lambda q: q.definition_text, word_obj.definitions.all())))
        # context['examples'] = ' - '.join(list(map(lambda q: q.example_text, word_obj.examples.all())))
        # context['object_list'] = WordModel.objects.all().prefetch_related('definitions', 'examples')
        context['page_title'] = f'{self.get_object().word_text}'
        return context


class WordCreateView(CreateView):
    model = WordModel
    form_class = WordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Word'
        return context

    def form_valid(self, form):
        # print(form.cleaned_data)
        word_obj = form.instance
        cleaned_data = form.cleaned_data
        definitions = cleaned_data['definition'].split('-')
        examples = cleaned_data['example'].split('-')
        pron_word_link = cleaned_data['pron_word_link']
        word_pron_audio_link = get_link_from_url(pron_word_link)
        word_obj.pron_word_link = word_pron_audio_link
        word_obj.save()
        # create definition model for all in the list
        for definition in definitions:
            DefinitionsModel.objects.create(word=word_obj, definition_text=definition.strip())
        for example in examples:
            ExampleModel.objects.create(word=word_obj, example_text=example.strip())
        messages.success(self.request, f'The {word_obj.word_text} word was created successfully')
        return super().form_valid(form)


class WordUpdateView(UpdateView):
    model = WordModel
    template_name_suffix = "_update"
    form_class = WordForm

    def get_initial(self):
        initial_data = super().get_initial()
        word_obj = self.get_object()
        initial_data['definition'] = ' - '.join(list(map(lambda q: q.definition_text, word_obj.definitions.all())))
        initial_data['example'] = ' - '.join(list(map(lambda q: q.example_text, word_obj.examples.all())))
        return initial_data

    def form_valid(self, form):
        # print(form.cleaned_data)
        word_obj = form.instance
        cleaned_data = form.cleaned_data
        definitions = cleaned_data['definition'].split('-')
        examples = cleaned_data['example'].split('-')
        pron_word_link = cleaned_data['pron_word_link']
        try:
            word_pron_audio_link = get_link_from_url(pron_word_link)
            word_obj.pron_word_link = word_pron_audio_link
        except:
            print("There's problem here")
        word_obj.save()
        # delete all the definitions and examples. I don't any way now to deal with update these data
        defs = word_obj.definitions.all()
        exas = word_obj.examples.all()
        defs.delete()
        exas.delete()
        # DefinitionsModel.objects.filter(word=word_obj).delete()
        # ExampleModel.objects.filter(word=word_obj).delete()
        # create definition model for all in the list
        for definition in definitions:
                DefinitionsModel.objects.create(word=word_obj, definition_text=definition.strip())
        for example in examples:
            ExampleModel.objects.create(word=word_obj, example_text=example.strip())
        return super().form_valid(form)


class WordDeleteView(DeleteView):
    model = WordModel
    success_url = reverse_lazy('theNewStore:word_list')

    def form_valid(self, form):
        messages.info(self.request, f"The {form.instance.word_text} was successfully deleted!")
        return super().form_valid(form)


def create_word(request):
    word_form = WordForm(request.POST or None)
    if word_form.is_valid():
        return redirect(reverse('theNewStore:word_list'))
    return render(request, 'words\word_form.html', context={'form': word_form})
