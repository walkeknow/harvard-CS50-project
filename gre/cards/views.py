from django.shortcuts import render, get_object_or_404
from .models import Word
import ast
from random import sample


# Create your views here.
def index(request):
    all_words = Word.objects.order_by('word')
    print(all_words)
    all_words = list(all_words)
    number_of_words = 50
    selected = sample(all_words, number_of_words)
    return render(request, 'cards/index.html', {'all_words': selected})


def detail(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    m_list = ast.literal_eval(word.means)
    print(m_list)
    meanings = {}
    for i in range(0, len(m_list)):
        print(i, m_list[i])
        meanings[str(i + 1)+'.'] = m_list[i]
    print(meanings)
    return render(request, 'cards/details.html', {'word': word, 'meanings': meanings})
