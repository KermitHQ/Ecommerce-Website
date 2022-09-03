
from .models import Order

def HasActiveOrder(user):
	try:
		order = Order.objects.get(user=user)
	except:
		return False

	if order:
		return True

def HasMadeOrder(user):
	try:
		order = Order.objects.get(user=user, made=True)
	except:
		return False

	if order:
		return True