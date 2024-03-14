from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    return render(request, "register.html")

def userLogin(request):
    errorMessage = None #Initialization of the error Message variable
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')
        User = authenticate(username=username, password=password)
        if User:
            login(request, User) #Authenticate and User Login
            #Redirection to page when successful login
            return render(request, 'question.html')
        else:
            errorMessage = 'Benutzername nicht gefunden oder falsches Passwort eingegeben.'
    context = {'error_Message': errorMessage} #Pass Error Message to Login.Html
    return render(request, 'login.html', context)


def menu(request):
    return render(request, 'menu.html')

def question(request):
    return render(request, 'question.html')