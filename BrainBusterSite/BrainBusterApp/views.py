from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == "POST":
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        # Validate Users Input
        if not username or not email or not password1 or not password2:
            messages.error(request, "Bitte alle Felder ausfüllen!")
            return render(request, "register.html")
        
        # Check if Users Input for Password is different
        if password1 != password2:
            # messages.error(request, "Passwörter stimmen nicht überein.", extra_tags="PasswordRegisterError")
            messages.add_message(request, messages.ERROR,"Passwörter stimmen nicht überein.", extra_tags="PasswordRegisterError")
            return render(request, "register.html")
        
        # Check for existing username && email
        if User.objects.filter(username=username).exists():
            messages.errror(request, "Benutzer bereits vergeben.")
            return render(request, "register.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-Mail-Adresse bereits vorhanden.")
            return render(request, "register.html")
        
        # Create new User in Users-Table
        user = User.objects.create_user(username, email, password1, firstname, lastname)
        user.save()
        
        #Registration sucessfull
        messages.success(request, "Registierung erfolgreich!")
        
        user = authenticate(username = username, password = password1)
        
        if user is not None:
            login(request, user)
            return render(request, "menu.html")
    
    return render (request, "register.html")
        
    
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')
        
        User_Credentials_Valid = authenticate(username=username, password=password)
        
        if User_Credentials_Valid:
            login(request, User_Credentials_Valid) #Authenticate and User Login
            #Redirection to page when successful login
            return render(request, 'menu.html')
        else:
            messages.add_message(request, messages.ERROR,'Benutzername nicht gefunden oder falsches Passwort eingegeben.', extra_tags="FalseUserNameORPassword")
            
    return render(request, "login.html", )

def menu(request):
    return render(request, 'menu.html')

def question(request):
    return render(request, 'question.html')
