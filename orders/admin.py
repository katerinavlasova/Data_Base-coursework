from django.contrib import admin
from .models import *
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
	model = ProductInOrder
	extra = 0

class ProductInBasketInline(admin.TabularInline):
	model = ProductInBasket
	extra = 0


class StatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]

	class Meta:
		model = Status


#admin.site.register(laptops)
admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	inlines = [ProductInOrderInline]
	class Meta:
		model = Order


#admin.site.register(laptops)
admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInOrder._meta.fields]
	class Meta:
		model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class BasketAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Basket._meta.fields]
	inlines = [ProductInBasketInline]
	class Meta:
		model = Basket


#admin.site.register(laptops)
admin.site.register(Basket, BasketAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInBasket._meta.fields]
	class Meta:
		model = ProductInBasket




admin.site.register(ProductInBasket, ProductInBasketAdmin)



