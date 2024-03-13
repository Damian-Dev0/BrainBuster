from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    return render(request, 'menu.html')

def question(request):
    return render(request, 'question.html')

def login(request):
    return render(request, 'login.html')