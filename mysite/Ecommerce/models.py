from django.db import models
from Account.models import Account
import os


class Order(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return (" {} active {}" if self.is_active else "{} not active {}").format(self.user.username, self.id)

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


def getFileNumber():
	queryset = Product.objects.all().order_by('pk')
	if queryset:
		last_id = len(queryset)
		file_number = last_id+1
		return str(file_number)
	else:
		file_number=1
		return str(file_number)
	
def getImageURL(instance, filename):
	path = os.path.join("products_images/{}/product_image.png".format(getFileNumber()))
	print(path)
	if os.path.isfile("media/" + path):
		print("image with this id already exist, ")
		os.remove("media/" + path)
		return path
	else:
		return path

class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	availability = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name

	#def get_product_image_filename(self):
	#	return str(self.image)[str(self.image).index(f'product_images/{self.pk}'):]

	#def get_url(self):
	#	return getProductImageURL(self.pk)

	image = models.ImageField(upload_to=getImageURL, default="static/default.png" )

	

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def accept_order(self):
		
		ordered_item = self.item
		self.item.availability -= self.quantity

	def __str__(self):
		return ("{}'s' order id: {} - {} - {}x".format(self.order.user.username, self.order.id, self.item, self.quantity))


