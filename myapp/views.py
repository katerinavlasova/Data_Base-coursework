from django.shortcuts import render
from .forms import *

def register(request):
	userform = RegistrationForm()
	return render(request, "register.html", {"form": userform})

def login(request):
	userform = LoginForm()
	return render(request, "login.html", {"form": userform})

def store(request):
	return render(request, "store.html")


def index(request):
	name = "Coding"
	current_day = "04.05.2020"
	form = CustomerForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		print(form.cleaned_data)
		new_form = form.save()
	return render(request, "index.html", locals())
