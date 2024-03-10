from django import forms
from .models import Category, Tag, Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.bootstrap import InlineCheckboxes

class ProductSearchForm(forms.Form):
	search_string = forms.CharField(label='Search', max_length=100, required=False)
	category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()

		self.helper.form_id = 'search_form'
		self.helper.form_class = 'search-filter-form mb-4'
		self.helper.form_method = 'GET'
		self.helper.use_custom_control = True 

		self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-dark mr-3'))

		self.helper.layout = Layout(
			'search_string', 
			'category',
			InlineCheckboxes('tags', css_class="tag-checkboxes")
		)