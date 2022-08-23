from django.forms import ModelForm
from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields='__all__'

	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields[ 'name' ].widget.attrs[ 'placeholder' ]="Enter product's name"
		self.fields[ 'name' ].label=""
		self.fields[ 'category' ].label=""
		self.fields[ 'availability' ].widget.attrs[ 'placeholder' ]="Set availability"
		self.fields[ 'availability' ].label=""
		self.fields[ 'price' ].widget.attrs[ 'placeholder' ]="Set price"
		self.fields[ 'price' ].label=""