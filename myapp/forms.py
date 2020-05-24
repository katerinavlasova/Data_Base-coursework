from django import forms
from myapp.models import *
from products.models import Reviews
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = [""]

class LoginForm(forms.Form):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())



class RegistrationForm(forms.Form):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required = True, widget = forms.EmailInput)
	password = forms.CharField(required=True, widget=forms.PasswordInput(),)
	repeat_password = forms.CharField(required=True, widget=forms.PasswordInput(),)
	def save(self, request):
		user = User.objects.create_user(
			cdata['first_name'],
			cdata['last_name'],
			cdata['email'],
			cdata['password'])
		user.save()
		profile = Profile.objects.create(user = user, first_name = cdata['first_name'], last_name = cdata['last_name'])
		profile.save()


class ReviewForm(forms.ModelForm):
	"""Otziv"""
	class Meta:
		model = Reviews
		fields = ("name", "email", "text")














