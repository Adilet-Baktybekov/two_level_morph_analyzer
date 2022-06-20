from django.shortcuts import render
import sys
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
      for w in words:
          ans = Word(w)
          res = ans.search_word_db(ans.change_word)
          root = ans.root
          part_of_speech = ans.part_of_speech
          all_symbols = ans.symbols_list
          all_endings = ans.symbols

          dict = {
              'word': word,
              'res': res,
              'root': root,
              'part_of_speech': part_of_speech,
              'all_symbols': all_symbols,
              'all_endings': all_endings
          }

          return render(request, 'analyzer_website/response.html', dict)


