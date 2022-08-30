from django.forms import ModelForm, inlineformset_factory
from .models import Product, Category, Photo
from django import forms



from PIL import Image
from django.core.files import File
from .models import Photo, Product

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

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('file',)




