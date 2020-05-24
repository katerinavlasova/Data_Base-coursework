from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0

class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline]
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

class ProductPhoneAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductPhone._meta.fields]
	inlines = [ProductImageInline]
	class Meta:
		model = ProductPhone

admin.site.register(ProductPhone, ProductPhoneAdmin)

class ProductLaptopAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductLaptop._meta.fields]
	inlines = [ProductImageInline]
	class Meta:
		model = ProductLaptop

admin.site.register(ProductLaptop, ProductLaptopAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]
	class Meta:
		model = ProductImage



#admin.site.register(laptops)
admin.site.register(ProductImage, ProductImageAdmin)


class ReviewsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Reviews._meta.fields]
	class Meta:
		model = Reviews

admin.site.register(Reviews, ReviewsAdmin)




