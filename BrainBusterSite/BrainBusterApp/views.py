from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    return render(request, 'menu.html')

def question(request):
    fragen = Question.objects.all()
    return render(request, 'question.html', {'fragen': fragen})

def login(request):
    return render(request, 'login.html')