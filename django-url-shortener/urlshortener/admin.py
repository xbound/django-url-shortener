from django.contrib import admin

from .models import Url
from .forms import UrlForm

@admin.register(Url)
class UrlModelAdmin(admin.ModelAdmin):
    form = UrlForm

