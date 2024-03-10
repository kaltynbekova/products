from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm

# Create your views here.
def index(request):
	products = Product.objects.all()
	form = ProductSearchForm(request.GET)

	if form.is_valid():
		qstring = form.cleaned_data.get('search_string')
		products = products.filter(title__icontains=qstring)

		qcategory = form.cleaned_data.get('category')
		if qcategory:
			products = products.filter(category=qcategory)

		qtags = form.cleaned_data.get('tags')
		if qtags:
			products = products.filter(tags__in=qtags)

	return render(request, 'index.html', {'products': products, 'form': form})