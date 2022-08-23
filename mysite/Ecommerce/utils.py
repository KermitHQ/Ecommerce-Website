
def getProductImageURL(pk):
	path = "media/products_images/" + str(pk) + "/product_image.png"
	return path


def getFileNumber():
	queryset = Product.objects.all().order_by('pk')
	last = queryset.last()
	last_id = last.id
	file_number = last_id+1
	return str(file_number)