
from .models import Order

def HasActiveOrder(user):
	try:
		order = Order.objects.get(user=user)
	except:
		return False

	if order:
		return True