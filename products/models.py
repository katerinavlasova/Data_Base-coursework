from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length = 30, null = True, default = None)
	copies = models.IntegerField(default = 0)
	brand = models.CharField(max_length=40, null = True, default = None)
	series = models.CharField(max_length=30, null = True, default = None)
	category_choices = [('Laptops', 'Laptop'), ('Phones', 'Phone')]
	category = models.CharField(max_length =10, choices = category_choices, blank = True, null = True, default = None)
	price = models.IntegerField(default = 0)
	discount = models.IntegerField(default = 0)
	is_active = models.BooleanField(default=True)
	color = models.CharField(max_length=10, null = True, default = None)
	weight = models.CharField(max_length=10, null = True, default = None)
	country = models.CharField(max_length=15, null = True, default = None)
	guarantee = models.CharField(max_length=10, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	url = models.SlugField(max_length=130, unique=True, blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "%s" % (self.name)
	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"slug": self.url})
	
	def get_products(self):
		Product.objects.filter(is_active=True).values("brand")
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
	
class ProductPhone(Product):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null = True, default = None, related_name = 'product_phone')
	screen = models.CharField(max_length = 25, null = True, default = None)
	dimensions = models.CharField(max_length = 25, null = True, default = None)
	os = models.CharField(max_length = 15, null = True, default = None)
	ROM = models.CharField(max_length = 10, null = True, default = None)
	bluetooth = models.IntegerField(default = 0)
	class Meta:
		verbose_name = 'Телефон'
		verbose_name_plural = 'Телефоны'

class ProductLaptop(Product):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null = True, default = None, related_name = 'product_laptop')
	os = models.CharField(max_length = 15, null = True, default = None)
	cpu = models.CharField(max_length = 15, null = True, default = None)
	cores = models.IntegerField(default = 0)
	memory_freq = models.CharField(max_length = 20, null = True, default = None)
	RAM = models.CharField(max_length = 20, null = True, default = None)
	resolution = models.CharField(max_length = 40, null = True, default = None)
	display_diagonal = models.CharField(max_length = 30, null = True, default = None)
	class Meta:
		verbose_name = 'Ноутбук'
		verbose_name_plural = 'Ноутбуки'

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null = True, default = None, related_name = 'productimage')
	image = models.ImageField(upload_to='products_images/', default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "%s" % (self.id)
	def one_item(self):
		return ProductImage.objects.get(is_active=True)
	class Meta:
		verbose_name = 'Фотография продукта'
		verbose_name_plural = 'Фотографии продуктов'

class ReviewsStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)
    def __str__(self):
        return f"{self.value}"
    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"



class Reviews(models.Model):
	"""Отзывы"""
	email = models.EmailField()
	name = models.CharField("Имя", max_length=100)
	text = models.TextField("Сообщение", max_length=5000)
	star = models.ForeignKey(ReviewsStar, on_delete=models.CASCADE, verbose_name="звезда", blank = True, null = True, default = None)
	product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return f"{self.name} - {self.product}"

	class Meta:
		verbose_name = "Отзыв"
		verbose_name_plural = "Отзывы"









