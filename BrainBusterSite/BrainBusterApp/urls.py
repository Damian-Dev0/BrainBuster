from django.urls import path

from . import views
from BrainBusterApp.views import menu, question, login, register

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu, name='menu'),
    path('question/', question, name='question'),
]