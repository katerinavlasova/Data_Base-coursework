from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.managers import *
# Create your models here.
#class laptops(models.Model):
 #   BRAND = models.CharField(max_length=40)
  #  OS = models.CharField(max_length=40)
   # SERIES = models.CharField(max_length=30)
    #CPU = models.CharField(max_length=40)
#    CORES = models.IntegerField()
#    MEMORY_FREQ = models.CharField(max_length=10)
#    RAM = models.CharField(max_length=10)
#    RESOLUTION = models.CharField(max_length=40)
#    DISPLAY_DIAGONAL = models.CharField(max_length=30)
#    COLOR = models.CharField(max_length=10)
#    WEIGHT = models.CharField(max_length=10)
#    COUNTRTY = models.CharField(max_length=15)
#    WARRANTY = models.CharField(max_length=10)



class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'user')
	first_name = models.CharField(max_length = 20, null = True, default = None)
	last_name = models.CharField(max_length = 20, null = True, default = None)
	email = models.EmailField()
	phone = models.CharField(max_length = 15, blank = True, null = True, default = None)
	address = models.CharField(max_length = 40, blank = True, null = True, default = None)
	objects = CustomerManager()	
	def __str__(self):
		return "%s %s" % (self.email, self.first_name)


