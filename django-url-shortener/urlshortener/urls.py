"""DjangoUrlShortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import default_view, shorten_url, go_to_url

app_name = 'urlshortener'

urlpatterns = [
    path('', default_view, name='default'),
    path('shorten', shorten_url, name='shorten'),
    path('<str:hashed_value>', go_to_url, name='go_to')
]
