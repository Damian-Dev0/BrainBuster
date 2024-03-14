from django.urls import path
from . import views
from BrainBusterApp.views import menu, question, userLogin, register

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu, name='menu'),
    path('question/', question, name='question'),
    path('login/', userLogin, name='login'),
    path("register/", register, name="register")
]