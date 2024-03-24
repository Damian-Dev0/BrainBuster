"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import path, include
from BrainBusterApp.views import menu, register

urlpatterns = [
    path('', include('BrainBusterApp.urls')),
    path('menu/', menu, name='menu'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/register/', register, name='register'),
]
