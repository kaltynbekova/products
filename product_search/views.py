from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
	products = Product.objects.all()
	query_string = request.GET['search_string'];
	if query_string:
		products = products.filter(title__icontains=query_string)
	return render(request, 'index.html', {'products': products})