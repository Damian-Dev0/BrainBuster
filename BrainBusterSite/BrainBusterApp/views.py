from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers

import random

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    return render(request, 'menu.html')

def question(request):
    fragen = Question.objects.all()
    zufall_frage = random.choice(fragen)
    antworten = zufall_frage.answers_set.all()
    return render(request, 'question.html', {'frage': zufall_frage, 'antworten': antworten})

def login(request):
    return render(request, 'login.html')