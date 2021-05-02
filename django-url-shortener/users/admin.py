from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdminForm(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("username", "admin")
    list_filter = ("admin", )
    fieldsets = (
        ("Personal info", {"fields": ("username",)}),
        ("Password", {"fields": ("password",)}),
        ("Permissions", {"fields": ("admin",)}),
    )

    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ()
