from django.db import models
from Account.models import Account
import os


class Order(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True) # if can be editted by user
	created = models.DateTimeField(auto_now_add=True)

	made = models.BooleanField(default=False) # if has been made by user
	paid = models.BooleanField(default=False) # if has beed paid by user
	complete = models.BooleanField(default=False) # if has been completed by admin/service

	def __str__(self):
		return (" {} active {}" if self.is_active else "{} not active {}").format(self.user.username, self.id)

	def getStatus(self):
		if self.is_active:
			return "active"
		elif self.made:
			return "made"
		elif self.paid:
			return "paid"
		elif self.complete:
			return "completed"
		else:
			return "Something went wrong"

	def getID(self):
		return ("#{}{}{}{}{}".format(self.user.id, self.created.day, self.created.month, self.created.year, self.id))

	def getItems(self):
		return OrderItem.objects.filter(order=self)
			

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def availableItems(self):
		return Product.objects.filter(category=self).count()

	
def getImageURL(instance, filename):
	path = os.path.join("products_images/{}/product_image.png".format(instance.product.id))
	
	if os.path.isfile("media/" + path):
		print("image with this id already exist, ")
		os.remove("media/products_images/{}".format(instance.product.id))
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

	def get_image_url(self):
		return Photo.objects.get(product=self).file.url



class Photo(models.Model):
	file = models.ImageField(upload_to=getImageURL, default="static/default.png")
	uploaded = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(self.pk)	

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def accept_order(self):
		
		ordered_item = self.item
		self.item.availability -= self.quantity

	def get_total_price(self):
		price = self.item.price * self.quantity
		return price

	def __str__(self):
		return ("{}'s' order id: {} - {} - {}x".format(self.order.user.username, self.order.id, self.item, self.quantity))

