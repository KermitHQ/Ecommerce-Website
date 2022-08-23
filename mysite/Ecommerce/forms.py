from django.forms import ModelForm
from .models import Product, Category
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

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder']="Enter category's name"
		self.fields['name'].label=""
