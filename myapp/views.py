from django.shortcuts import render
from .forms import CustomerForm

def register(request):
	if request.POST:
		form = RegisterForm(request.POST)
	if form.is_valid():
		form.save(request)
		return redirect("register.html")
	else:
		form = RegisterForm()
	return render(request, "index.html", {'form': form})


def index(request):
	name = "Coding"
	current_day = "04.05.2020"
	form = CustomerForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		print(form.cleaned_data)
		new_form = form.save()
	return render(request, "index.html", locals())
