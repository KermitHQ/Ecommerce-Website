from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Account

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Enter Email'}), label="")
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Enter Password'}), label="")

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = Account
		fields = ['username', 'email', 'password1', 'password2']
		

	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields[ 'username' ].widget.attrs[ 'placeholder' ]="Enter username"
		self.fields[ 'username' ].label=""
		self.fields[ 'email' ].widget.attrs[ 'placeholder' ]="Enter email"
		self.fields[ 'email' ].label=""
		self.fields[ 'password1' ].widget.attrs[ 'placeholder' ]="Enter password"
		self.fields[ 'password1' ].label=""
		self.fields[ 'password2' ].widget.attrs[ 'placeholder' ]="Confirm password"
		self.fields[ 'password2' ].label=""
		
		