from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	group = models.CharField(max_length=50, default='other')

	def __str__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)

	def __str__(self):
		return self.title