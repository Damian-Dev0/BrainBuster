from django.urls import path

from . import views
from BrainBusterApp.views import menu

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/', menu),
]