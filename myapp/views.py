from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
from products.models import Product, ProductPhone, ProductLaptop, Reviews
from orders.models import Order, ProductInOrder, Basket, ProductInBasket, Status
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

class OrderListView(View):
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
		orders = Order.objects.all()
		orders = orders.filter(customer_id = request.user.id)
		#product_in = ProductInOrder.objects.all()#filter(order_id = orders_id)
		#product = Product.objects.filter(id = product_in_id)
		product= Product.objects.all()
		data = {"order_list": orders, "products": product}
	#	print(User.id)
		return render(request, "order.html", data)#{"order_list": order})

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
		print(Basket.customer_id)
		basket = Basket.objects.filter(customer_id = request.user.id)
		#product_in = ProductInOrder.objects.all()#filter(order_id = orders_id)
		#product = Product.objects.filter(id = product_in_id)
		product= Product.objects.all()
	#	print(User.id)
		return render(request, "wishlist.html", {"basket_list": basket})#{"order_list": order})

def add_to_basket(request, slug):
	item = get_object_or_404(Product, slug = slug)
	basket_item, created = ProductInBasket.objects.get_or_create(product=item, customer_id=request.user.id)
	basket_qs = Basket.objects.filter(customer_id=request.user.id)
	if basket_qs.exists():
		basket = basket_qs[0]
		#check if the item is in order
		if ProductInBasket.objects.filter(product__slug=item.slug).exists():
			messages.info(request, "Вы добавили этот товар в желаемое:)")
			basket_item.number += 1
			basket_item.price_per_item = Product.objects.get(slug=slug).price
			basket_item.basket = basket_qs[0]
			basket_item.save()
			print("11 basket")
			return redirect("product_detail", slug=slug)
		else:
			messages.info(request, "Вы добавили этот товар в желаемое:)")
			basket_item.basket = basket_qs[0]
			basket_item.price_per_item = Product.objects.get(slug=slug).price
			basket_item.number = 1
			print("222")
			basket_item.price_per_item = Product.objects.get(slug=slug).price
			basket_item.save()
			return redirect("product_detail", slug=slug)
	else:
		print("333")
		ordered_date = timezone.now()
		messages.info(request, "Вы добавили этот товар в желаемое:)")
		newbasket = Basket.objects.create(customer_id=request.user.id, created = ordered_date)
		basket_item.basket = newbasket
		basket_item.price_per_item = Product.objects.get(slug=slug).price
		basket_item.save()
		return redirect("product_detail", slug=slug)

def remove_from_basket(request, slug):
	item = get_object_or_404(Product, slug = slug)
	basket_item = ProductInBasket.objects.get(product=item, customer_id=request.user.id)
	basket_qs = Basket.objects.filter(customer_id=request.user.id)
	print("removeee")
	if basket_qs.exists():
		basket = basket_qs[0]
		#check if the item is in order
		if ProductInOrder.objects.filter(product__slug=item.slug).exists():
			messages.info(request, "Вы удалили этот товар из желаемого:(")
			basket_item.delete()
			return redirect("product_detail", slug=slug)
	else:
		print("333")
		return redirect("product_detail", slug=slug)

def ordered(request):
	#pk = request.GET.get('pk') 
	order = Order.objects.filter(customer_id=request.user.id)
	if request.GET:
		#order.status_id=4
		#order.commets = comment
		comment = request.GET.get("comment")
		print(comment)
		order.update(status_id=4, commets=comment)
		return render(request, 'order.html')

def add_to_order(request, slug):
	item = get_object_or_404(Product, slug = slug)
	order_item, created = ProductInOrder.objects.get_or_create(product=item, customer_id=request.user.id)
	order_qs = Order.objects.filter(customer_id=request.user.id)
	if order_qs.exists():
		order = order_qs[0]
		#check if the item is in order
		if ProductInOrder.objects.filter(product__slug=item.slug).exists():
			messages.info(request, "Вы добавили этот товар в заказ:)")
			order_item.number += 1
			if order_item.order != order_qs[0]:
				order_item.order = order_qs[0]
			order_item.save()
			price = order_qs[0].total_price
			print(price)
			order_qs.update(total_price = price + order_item.price_per_item)
			print("11!!!!!")
			return redirect("product_detail", slug=slug)
		else:
			messages.info(request, "Вы добавили этот товар в заказ:)")
			order_item.order = order_qs[0]
			price = order_qs[0].total_price
			print(price)
			order_qs.update(total_price = price + order_item.price_per_item)
			order_item.number = 1
			order_item.save()
			print("222")
			#order_item.price_per_item = Product.objects.get(slug=slug).price
			return redirect("product_detail", slug=slug)
	else:
		print("333")
		status = Status.objects.all()
		ordered_date = timezone.now()
		messages.info(request, "Вы добавили этот товар в заказ:)")
		neworder = Order.objects.create(customer_id=request.user.id, created = ordered_date, status_id=3)
		price = neworder.total_price + order_item.price_per_item
		print(price)
		neworder.total_price = price
		neworder.save()
		order_item.order = neworder
		order_item.number = 1
		order_item.save()
		return redirect("product_detail", slug=slug)

def remove_from_order(request, slug):
	item = get_object_or_404(Product, slug = slug)
	order_item = ProductInOrder.objects.get(product=item, customer_id=request.user.id)
	order_qs = Order.objects.filter(customer_id=request.user.id)
	print("removeee")
	if order_qs.exists():
		order = order_qs[0]
		#check if the item is in order
		if ProductInOrder.objects.filter(product__slug=item.slug).exists():
			if order_item.number > 1:
				order_item.number -= 1
				order_item.order = order_qs[0]
				order_item.save()
				price = order_qs[0].total_price
				print(price)
				order_qs.update(total_price = price - order_item.price_per_item)
				#order_qs.update(total_price = order.total_price - order_item.total_price)
				messages.info(request, "Вы удалили этот товар из заказа:(")
				print("11")
				return redirect("product_detail", slug=slug)
			else:
				messages.info(request, "Вы удалили этот товар из заказа:(")
				order_item.order = None
				order_item.number = 0
				price = order_qs[0].total_price
				print(price)
				order_qs.update(total_price = price - order_item.price_per_item)
				order_item.delete()
				return redirect("product_detail", slug=slug)
	else:
		print("333")
		return redirect("product_detail", slug=slug)


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
	paginate_by = 10
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
	slug_field ="slug"
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

class Search(ShowFilters, ListView):
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
