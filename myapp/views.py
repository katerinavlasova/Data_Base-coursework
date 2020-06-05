from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json
from products.models import Product, ProductPhone, ProductLaptop, Reviews
from orders.models import Order, ProductInOrder
from myapp.models import Customer
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q
#def register(request):
#	userform = RegistrationForm(request.POST)
#	return render(request, "register.html", {"form": userform})

def register(request):
	if request.POST:
		form = RegisterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(request)
			return redirect('index')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

def login(request):
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			cdata = form.cleaned_data
			user = auth.authenticate(
				username=cdata['last_name'],
				first_name=cdata['first_name'],
				password=cdata['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		form.add_error('username', "Wrong username or password")
	else:
		userform = LoginForm()
	return render(request, "login.html", {"form": userform})

def logout(request):
	auth.logout(request)
	return redirect("index")


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

class WishListView(View):
	"""Список product in wishlist"""
	#model = Order
	#queryset = Order.objects.all()
	#iid = User.id
	#queryset = Order.objects.filter(Order.customer_id = User.get_id())
	#template_name = "store.html"
	#queryset = Order.objects.filter(customer = )
	#context_object_name='order_list'
	#template_name = 'wishlist.html'

	def get(self, request):
		#User.objects.filter(username = Order.customer)#Order.objects.filter(customer=User.get_username(self, request))
		print("HELLLOO")
		current_user = request.user.id
		print(current_user)
		print(Order.customer_id)
		order = Order.objects.filter(customer_id = request.user.id)
		#product_in = ProductInOrder.objects.filter(order_id = order.id)
		product = Product.objects.all()
		data = {"order_list": order, "products": product}
	#	print(User.id)
		return render(request, "wishlist.html", data)#{"order_list": order})

class ShowFilters:
	def filter_brand(self):
		return Product.objects.filter(is_active=True).distinct("brand")
	def filter_category(self):
		return Product.objects.filter(is_active=True).distinct("category")
	def get_first_five(self):
		return Product.objects.filter(is_active=True)


class ProductView(ShowFilters, ListView):
	"""Список product"""
	model = Product
	paginate_by = 4
	#queryset = Product.objects.all()
	#template_name = "store.html"
	queryset = Product.objects.filter(is_active=True)
	context_object_name='product_list'
	template_name = 'store.html'
	#def get(self, request):
	#	product = Product.objects.filter(is_active=True)
	#	return render(request, "store.html", {"product_list": product})

class ProductDetailView(ShowFilters, DetailView):
	"""Конкретный product"""
	model = Product
	slug_field ="url"
	context_object_name = 'product'
	template_name = 'product.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["star_form"] = ReviewForm()
		return context
	#def get(self, request, slug):
	#	product = Product.objects.get(url=slug)
	#	return render(request, "product.html", {"product": product})

class FilterProductsView(ShowFilters, ListView):
	template_name='store.html'
	#paginate_by = 1
	def get_queryset(self):
		queryset = Product.objects.filter(is_active=True)
		if "category" in self.request.GET:
			queryset = queryset.filter(category__in=self.request.GET.getlist("category"))
		if "brand" in self.request.GET:
			queryset = queryset.filter(brand__in=self.request.GET.getlist("brand"))
		if "min_price" in self.request.GET:
			minp = self.request.GET.get("min_price")
			queryset = queryset.filter(price__gte=minp)
		if "max_price" in self.request.GET:
			maxp = self.request.GET.get("max_price")
			queryset = queryset.filter(price__lte=maxp)
		return queryset
#		kwargs = {}
#		if self.request.GET.getlist("category"):
#			kwargs["category__in"] = self.request.GET.getlist("category")
#		if self.request.GET.getlist("brand"):
#			kwargs["brand__in"] = self.request.GET.getlist("brand")
#		return Product.objects.filter(**kwargs)

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
