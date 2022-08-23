from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

def registerView(request):
	context = {}
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			email = request.POST['email']
			password = request.POST['password1']
			user = authenticate(request, username=email, password=password)
			if user:
				login(request, user)
				return redirect('home')
	else:
		print("request method is not correct")
		form = UserRegisterForm()
	context['form'] = form
	return render(request, "Account/register.html", context)

