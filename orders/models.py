from django.db import models
from products.models import Product, ProductPhone, ProductLaptop
from myapp.models import Customer
from django.db.models.signals import post_save
from model_utils import Choices
# Create your models here.

class Status(models.Model):
	RESERVED = "RES" 
	NEW = "NEW"
	CANCELED = "CANC"
	CLOSED = "CLOS"
	status_choices = (
	(RESERVED, "Корзина"),
	(NEW, "Новый заказ"),
	(CANCELED, "Отменённый заказ"),
	(CLOSED, "Закрытый заказ"),
	)

	name = models.CharField(max_length = 20, choices = status_choices, default = RESERVED)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "Статус %s" %self.name

	class Meta:
        	verbose_name = 'Статус заказа'
        	verbose_name_plural = 'Статусы заказа'

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default = None,  related_name = 'customer')
	total_price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0) #total price for everytinh in order
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	commets = models.TextField(blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "Заказ %s статус %s" % (self.id, self.status.name)
	class Meta:
		ordering = ['-created']
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
	def save(self, *args, **kwargs):
		super(Order, self).save(*args, **kwargs)
	




class ProductInOrder(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank = False, null = True, default = None,  related_name ='in_order')
	product = models.ForeignKey(Product, on_delete= models.CASCADE, blank = False, null = True, default = None,  related_name ='productinorder')
	number = models.IntegerField(default = 0)
	is_active = models.BooleanField(default=True)
	price_per_item = models.PositiveIntegerField(default = 1)
	total_price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0) #price * number
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return "%s" % (self.product.name)
	class Meta:
		verbose_name = 'Товар в заказе'
		verbose_name_plural = 'Товары в заказе'
	def get_cost(self):
		return self.number * self.price_per_item
	def save(self, *args, **kwargs):
		price_per_item = self.product.price
		self.price_per_item = price_per_item
		self.total_price = self.number * price_per_item
		super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_postsave(sender, instance, created, **kwargs):
		order = instance.order
		all_products_in_order = ProductInOrder.objects.filter(order= order, is_active = True)
		order_total_price = 0
		for item in all_products_in_order:
			order_total_price += item.total_price
		instance.order.total_price = order_total_price 
		instance.order.save(force_update = True)


post_save.connect(product_in_order_postsave, sender = ProductInOrder)	

