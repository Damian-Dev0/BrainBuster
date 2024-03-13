from django.urls import path

from . import views
from BrainBusterApp.views import menu
from BrainBusterApp.views import question
from BrainBusterApp.views import login

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu),
    path('question/', question),
    path('login/', login),
]