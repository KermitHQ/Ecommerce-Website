from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Order, OrderItem
from django.views.generic.list import ListView
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required

@login_required
def CartView(request):
	context = {}
	order = Order.objects.get(user=request.user)
	ordered_products = OrderItem.objects.filter(order=order)
	
	total_price = 0
	for product in ordered_products:
		total_price += product.get_total_price()

	context['total_price'] = total_price
	context['order'] = order
	context['ordered_products'] = ordered_products
	return render(request, "Ecommerce/cart.html", context)


def AvailableItemsList(request, category=None):
	context = {}
	categories = Category.objects.all()
	context['categories'] = categories
	min_price = request.GET.get('price_from', '') or None
	max_price = request.GET.get('price_to', '') or None
	sorted = request.GET.get('sorted', '') or None
	if category is not None:
		object_list = Product.objects.all().filter(category__name=category)
	else:
		object_list = Product.objects.all()

	if min_price is not None:
		object_list = object_list.filter(price__gte=min_price)

	if min_price is not None:
		object_list = object_list.filter(price__lte=max_price)

	if sorted is not None:
		print(sorted)
		if sorted == 'reverse':
			object_list = object_list.order_by('-price')
		elif sorted == 'normal':
			object_list = object_list.order_by('price')

	

	context['object_list'] = object_list 

	return render(request,"Ecommerce/home.html", context)


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

@login_required
def AddToCartView(request, product_id):
	#order = Order.objects.get_or_create(user=request.user)
	try:
		order = Order.objects.get(user=request.user, is_active=True)
	except Order.DoesNotExist:
		order = Order.objects.create(user=request.user, is_active=True)
		order.save()
	item = Product.objects.get(id=product_id)
	print()
	try:
		print(order)
		print(item)
		print("sadasd")
		orderItem = OrderItem.objects.get(order=order, item=item)
		orderItem.quantity += 1
		orderItem.save()
	except OrderItem.DoesNotExist:
		orderItem = OrderItem.objects.create(order=order, item=item, quantity=1)
	return redirect('home')