from django.shortcuts import render, redirect
from .forms import *
from products.models import Product, ProductPhone, ProductLaptop, Reviews
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.db.models import Q

def register(request):
	userform = RegistrationForm()
	return render(request, "register.html", {"form": userform})

def login(request):
	userform = LoginForm()
	return render(request, "login.html", {"form": userform})

def store(request):
	return render(request, "store.html")

class AddReview(View):
	def post(self, request, pk):
		form = ReviewForm(request.POST)
		product = Product.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			form.product = product
			form.save() 
		return redirect(product.get_absolute_url())

class ProductView(View):
	"""Список product"""
	#model = Product
	#queryset = Product.objects.all()
	#template_name = "store.html"
	paginate_by = 2
	def get(self, request):
		product = Product.objects.filter(is_active=True)
		return render(request, "store.html", {"product_list": product})

class ProductDetailView(View):
	"""Конкретный product"""
	def get(self, request, slug):
		product = Product.objects.get(url=slug)
		return render(request, "product.html", {"product": product})

class Search(ListView):
	model = Product
	template_name="search.html"
	def get_queryset(self):
		# Получаем не отфильтрованный кверисет всех моделей
		queryset = Product.objects.all()
		q = self.request.GET.get("q")
		if q:
			# Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
			    return queryset.filter(Q(name__icontains=q))# | Q(post__icontains=q))
		return queryset


def index(request):
	name = "Coding"
	current_day = "04.05.2020"
	form = CustomerForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		print(form.cleaned_data)
		new_form = form.save()
	return render(request, "index.html", locals())
