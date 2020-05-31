from django import forms
from myapp.models import *
from products.models import Reviews, ReviewsStar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = [""]

class LoginForm(forms.Form):
	first_name = forms.CharField(required=True, label='Имя')
	last_name = forms.CharField(required=True, label = 'Фамииля')
	password = forms.CharField(required=True, label ='Пароль', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required = True, widget = forms.EmailInput)
	password = forms.CharField(required=True, widget=forms.PasswordInput(),)
	repeat_password = forms.CharField(required=True, widget=forms.PasswordInput(),)
	def clean_email(self):
		email = self.cleaned_data.get('email', '')
		if email == "":
			return email
		if email.find('@') < 1 or len(email) < 3:
			raise forms.ValidationError('Некорректный email')
		try:
			_ = User.objects.get(email=email)
			raise forms.ValidationError('Пользователь с таким email уже существует')
		except User.DoesNotExist:
			return email
	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name', '')
		if len(first_name) > 30:
			raise forms.ValidationError(
			'Имя должно быть короче 30 символов')
		if len(first_name) < 1:
			raise forms.ValidationError('Имя должно быть больше 1 символа')
		return first_name
	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name', '')
		if len(last_name) > 30:
			raise forms.ValidationError(
			'Фамилимя должна быть короче 30 символов')
		if len(last_name) < 1:
			raise forms.ValidationError('Фамилия должна быть больше 1 символа')
		try:
			_ = User.objects.get(username=last_name)
			raise forms.ValidationError('User with the same nickname is exist')
		except User.DoesNotExist:
			return last_name
	def clean_password(self):
		password = self.cleaned_data.get('password', '')
		if len(password) < 4:
			raise forms.ValidationError('Пароль должен быть не меньше 4 символов')
		return password
	def clean_repeat_password(self):
		repeat_password = self.cleaned_data.get('repeat_password', '')
		password = self.cleaned_data.get('password', '')
		if repeat_password != password:
			raise forms.ValidationError('Пароли не совпадают')
		return repeat_password

	def save(self, request):
		cdata = self.cleaned_data
		user = User.objects.create_user(
			self.cleaned_data['last_name'],
			first_name=self.cleaned_data['first_name'],
			last_name=self.cleaned_data['last_name'],
			email=self.cleaned_data['email'],
			password=self.cleaned_data['password'])
			#cdata['last_name'],
			#cdata['first_name'],
			#cdata['email'],
			#cdata['password'])
		user.save()
		profile = Customer.objects.create(user = user, first_name = cdata['first_name'], last_name = cdata['last_name'], email = cdata['email'], password = cdata['password'])
		profile.save()


class ReviewForm(forms.ModelForm):
	"""Otziv"""
	class Meta:
		model = Reviews
		fields = ("name", "email", "text", "star",)

class RatingForm(forms.ModelForm):
	star = forms.ModelChoiceField(queryset = ReviewsStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)
	class Meta:
		model = Reviews
		fields=("star",)













