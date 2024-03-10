from django.shortcuts import render
from django.db.models import Q
from .models import Product
from .forms import ProductSearchForm

# Create your views here.
def index(request):
	products = Product.objects.all()
	form = ProductSearchForm(request.GET)

	if form.is_valid():
		qstring = form.cleaned_data.get('search_string')
		if qstring:
			qtext = None
			for word in qstring.split(" "):
				qword = Q( title__icontains = word ) | Q( category__name__icontains = word ) | Q( tags__name__icontains = word)
				qtext = (qtext & qword) if qtext else qword		
			products = products.filter( qtext ).distinct() 

		qcategory = form.cleaned_data.get('category')
		if qcategory:
			products = products.filter(category=qcategory)

		qtags = form.cleaned_data.get('tags')
		if qtags:
			products = products.filter(tags__in=qtags)

	return render(request, 'index.html', {'products': products, 'form': form})