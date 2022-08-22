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

def getImageURL(self, filename):
	path = "media/products_images/" + str(self.pk) + "/product_image.png"
	return path



class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	availability = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)

	image = models.ImageField(default="media/static/products_images/default.png", upload_to=getImageURL)

	def __str__(self):
		return self.name

	def get_product_image_filename(self):
		return str(self.image)[str(self.image).index(f'product_images/{self.pk}'):]

	

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def accept_order(self):
		
		ordered_item = self.item
		self.item.availability -= self.quantity

	def __str__(self):
		return ("{}'s' order id: {} - {} - {}x".format(self.order.user.username, self.order.id, self.item, self.quantity))


