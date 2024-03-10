from django.shortcuts import render
from django.db.models import Q, Count
from .models import Product
from .forms import ProductSearchForm

# Create your views here.
def index(request):
	products = Product.objects.all()

	if 'reset' in request.GET:
		return render(request, 'index.html', {'products': products, 'form': ProductSearchForm()})

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
			rule = form.cleaned_data.get('tags_filter_rules')
			if rule == "all":
				#product must match all selected tags
				tagged_products = products.annotate(c=Count('tags')).filter(c__gte=len(qtags))
				for tag in qtags:
					tagged_products = tagged_products.filter(tags=tag)
				products = tagged_products
			elif rule == "none":
				#product must not include any of the selected tags
				products = products.exclude(tags__in=qtags)
			else:
				# product can match at least one of selected tags
				products = products.filter(tags__in=qtags)

	return render(request, 'index.html', {'products': products, 'form': form})
