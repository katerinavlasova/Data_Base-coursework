from django.db import models

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length = 30, null = True, default = None)
	brand = models.CharField(max_length=40, null = True, default = None)
	series = models.CharField(max_length=30, null = True, default = None)
	price = models.IntegerField(default = 0)
	color = models.CharField(max_length=10, null = True, default = None)
	weight = models.CharField(max_length=10, null = True, default = None)
	country = models.CharField(max_length=15, null = True, default = None)
	guarantee = models.CharField(max_length=10, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "%s" % (self.name)
	
class ProductPhone(Product):
	is_active = models.BooleanField(default=True)
	screen = models.CharField(max_length = 25, null = True, default = None)
	dimensions = models.CharField(max_length = 25, null = True, default = None)
	os = models.CharField(max_length = 15, null = True, default = None)
	ROM = models.CharField(max_length = 10, null = True, default = None)
	bluetooth = models.IntegerField(default = 0)
	class Meta:
		verbose_name = 'Телефон'
		verbose_name_plural = 'Телефоны'

class ProductLaptop(Product):
	os = models.CharField(max_length = 15, null = True, default = None)
	is_active = models.BooleanField(default=True)
	cpu = models.CharField(max_length = 15, null = True, default = None)
	cores = models.IntegerField(default = 0)
	memory_freq = models.CharField(max_length = 20, null = True, default = None)
	RAM = models.CharField(max_length = 20, null = True, default = None)
	resolution = models.CharField(max_length = 40, null = True, default = None)
	display_diagonal = models.CharField(max_length = 30, null = True, default = None)

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null = True, default = None)
	image = models.ImageField(upload_to='products_images/', default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "%s" % (self.id)
