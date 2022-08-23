from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Enter Email'}), label="")
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Enter Password'}), label="")