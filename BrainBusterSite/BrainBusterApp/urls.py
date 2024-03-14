from django.urls import path

from . import views
from BrainBusterApp.views import menu
from BrainBusterApp.views import question
from BrainBusterApp.views import login

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu, name='menu'),
    path('question/', question, name='question'),
    path('login', login, name='login'),
]