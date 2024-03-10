from django import forms
from .models import Category, Tag, Product

class ProductSearchForm(forms.Form):
	search_string = forms.CharField(label='Search', max_length=100, required=False)
	category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)