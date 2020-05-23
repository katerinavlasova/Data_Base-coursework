
from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Customer._meta.fields]



#admin.site.register(laptops)
admin.site.register(Customer, CustomerAdmin)


