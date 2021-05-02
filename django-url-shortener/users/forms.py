from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    ReadOnlyPasswordHashField,
    UserChangeForm,
    UserCreationForm,
)
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import User


class CreateUserForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password", "admin")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise ValidationError(_("Username already exists"))

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ChangeUserForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("username", "password", "admin")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
