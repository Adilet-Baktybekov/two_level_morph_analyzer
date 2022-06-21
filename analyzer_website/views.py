from django.shortcuts import render
import sys
import os
sys.path.append('../backend/main_analyzer.py')
from backend.main_analyzer import Word
from .models import *

def home(request):
    return render(request, 'analyzer_website/main.html')

def about(request):
    all_content_kg = KyrgyzLang.objects.all()
    all_modal_window = ModalWindow.objects.all()
    print(all_modal_window)
    return render(request, 'analyzer_website/about.html', {'all_content_kg': all_content_kg, 'all_modal_window': all_modal_window})

def analyzer(request):
      return render(request, 'analyzer_website/analyzer.html')

def validate(request):
   if request.method == 'POST':
      word = request.POST["words"]
      words = word.split(' ')
      all_res = ''
      for w in words:
          ans = Word(w)
          res = ans.search_word_db(ans.change_word)
          all_res += res + "\n"
      dict = {
          'word': word,
          'res': all_res

      }

      return render(request, 'analyzer_website/response.html', dict)


