from django.urls import path

from . import views
from BrainBusterApp.views import menu, question, rankings

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu, name='menu'),
    path('question/', question, name='question'),
    path('rankings/', rankings, name='rankings'),
]