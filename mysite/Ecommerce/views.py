from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product, Category, Order, OrderItem, Photo
from django.views.generic.list import ListView
from .forms import ProductForm, CategoryForm, PhotoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .utils import HasActiveOrder


@login_required
def CartView(request):
	
	context = {}
	order = Order.objects.get(user=request.user)
	ordered_products = OrderItem.objects.filter(order=order)
	
	total_price = 0
	for product in ordered_products:
		total_price += product.get_total_price()

	TOTAL_price = 0
	for item in order.orderitem_set.all():
		TOTAL_price += item.get_total_price()
	
	
	context['TOTAL'] = TOTAL_price
	context['total_price'] = total_price
	context['order'] = order
	context['ordered_products'] = ordered_products
	return render(request, "Ecommerce/cart.html", context)


def AvailableItemsList(request, category=None, page=None):
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
		if sorted == 'reverse':
			object_list = object_list.order_by('-price')
		elif sorted == 'normal':
			object_list = object_list.order_by('price')

	#context['object_list'] = object_list 
	paginator = Paginator(object_list, 3)
	objects_count = object_list.count()
	context['objects_count'] = objects_count
	page_number = page
	page_obj = paginator.get_page(page_number)
	context['page_obj'] = page_obj


	return render(request,"Ecommerce/home.html", context)


@login_required
def ProductDeleteView(request, product_id):
	if request.user.is_superuser:
		product = get_object_or_404(Product, id=product_id)
		product.delete()
	else:
		print("You are not allowed here")
	return redirect('home')

@login_required
def deleteOrderItem(request, orderitem_id):
	Orderitem = OrderItem.objects.get(id=orderitem_id)
	if request.user == Orderitem .order.user:
		Orderitem.delete()
	else:
		print("You are not allowed here")
	return redirect('cart')


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
def AddProduct(request):
	
	if HasActiveOrder(request.user):
		print("You have at least one unpaid order")
		return redirect('cart')
	
	
	if request.method == 'GET':
		product_id = request.GET['product_id']
		product = Product.objects.get(id=product_id)
		try:
			order = Order.objects.get(user=request.user, is_active=True)
		except Order.DoesNotExist:
			order = Order.objects.create(user=request.user, is_active=True)
			order.save()

		try:
			orderitem = OrderItem.objects.get(order=order, item=product)
			print('item found')
			orderitem.quantity += 1
			orderitem.save()
		except OrderItem.DoesNotExist:
			orderitem = OrderItem(order=order, item=product, quantity=1)
			orderitem.save()
		return redirect('cart')
	else:
		return HttpResponse("Request method is not a GET")

@login_required
def increaseQuantity(request):
	orderItemId = request.POST.get('orderItem_id')
	if request.method == 'POST':
		if request.POST.get("operation") == "increase":
			orderitem = OrderItem.objects.get(id=orderItemId)
			orderitem.quantity += 1
			orderitem.save()
			return JsonResponse({'count':orderitem.quantity})
	return JsonResponse({'error':'error'})

@login_required
def decreaseQuantity(request):
	if request.method == 'POST':
		if request.POST.get("operation") == "decrease":
			orderitem = OrderItem.objects.get(id=request.POST.get('orderItem_id', None))
			orderitem.quantity -= 1
			if orderitem.quantity <= 0:
				orderitem.delete()
			else:
				orderitem.save()
			return JsonResponse({'count':orderitem.quantity})
	return JsonResponse({'error':'error'})

@login_required
def makeOrder(request, order_id):
	order = Order.objects.get(id=order_id)
	if request.user == order.user:
		order.is_active = False
		order.made = True
		order.save()
		print("order has been made")
	else:
		print("You are not allowed here")
	return redirect('cart')

@login_required
def cancelOrder(request, order_id):
	order = Order.objects.get(id=order_id)
	if request.user == order.user:
		order.is_active = True
		order.made = False
		order.save()
		print("order has been canceled")
	else:
		print("You are not allowed here")
	return redirect('cart')


@login_required
def ProductCreateView(request):
	context = {}
	created_product=None

	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			created_product = form.save()
			print("successfully created new product")
		else:
			print("product form is not valid")
			print(form.errors)
	else:
		print("form is not valid")
		
	context['form'] = form

	form2 = PhotoForm()
	if request.method == 'POST':
		form2 = PhotoForm(request.POST or None, request.FILES or None)
		if form2.is_valid():
			obj = form2.save(commit=False)
			obj.product = created_product
			obj.save()
			print("Created new photo with {} product".format(obj.product))
			#return JsonResponse({'message': 'works'})
			
	context['form2'] = form2

	return render(request, "Ecommerce/create_product.html", context)



