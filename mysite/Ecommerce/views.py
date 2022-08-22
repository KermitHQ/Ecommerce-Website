from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.generic.list import ListView
from .forms import ProductForm

def CartView(request):
	pass

def AvailableItemsList(request):
	items = Product.objects.filter(availability>0)

	return render(request, )

class ProductListView(ListView):
	model = Product
	
	template_name = "Ecommerce/home.html"

def ProductCreationView(request):
	context = {}
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			print('form is not valid')
	else:
		print('request method is not correct')
	context['form'] = form

	return render(request, "Ecommerce/create_product.html", context)

def ProductDeleteView(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	product.delete()
	return redirect('home')
