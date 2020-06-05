from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.managers import *




class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True, default = None, related_name= 'user')
	first_name = models.CharField(max_length = 20, null = True, default = None)
	last_name = models.CharField(max_length = 20, null = True, default = None)
	email = models.EmailField(blank = True, null = True, default = None)
	phone = models.CharField(max_length = 15, blank = True, null = True, default = None)
	address = models.CharField(max_length = 40, blank = True, null = True, default = None)
	objects = CustomerManager()	
	def __str__(self):
		return "%s %s" % (self.email, self.first_name)
	def user_name(self):
		return self.get_username()


