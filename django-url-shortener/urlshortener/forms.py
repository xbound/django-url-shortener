from django import forms
from .models import Url


class UrlForm(forms.ModelForm):

    hashed_url = forms.CharField(disabled=True)

    class Meta:
        model = Url
        fields = '__all__'

