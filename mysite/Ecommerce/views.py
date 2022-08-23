from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.generic.list import ListView
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required


def CartView(request):
	pass

def AvailableItemsList(request):
	items = Product.objects.filter(availability>0)

	return render(request, )

class ProductListView(ListView):
	model = Product
	
	template_name = "Ecommerce/home.html"

@login_required
def ProductCreationView(request):
	context = {}
	form = ProductForm()
	if request.user.is_superuser:
		if request.method == 'POST':
			form = ProductForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('home')
			else:
				print('form is not valid')
		else:
			print('request method is not correct')
	else:
		print("You are not allowed here")
		return redirect('home')
	context['form'] = form

	return render(request, "Ecommerce/create_product.html", context)

@login_required
def ProductDeleteView(request, product_id):
	if request.user.is_superuser:
		product = get_object_or_404(Product, id=product_id)
		product.delete()
	else:
		print("You are not allowed here")
	return redirect('home')

@login_required
def CategoryCreationView(request):
	context = {}
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context['form'] = form

	return render(request, "Ecommerce/create_category.html", context)
