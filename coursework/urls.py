"""coursework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', views.register, name ="register"),
	path('login/', views.login, name ="login"),

	path('search/', views.Search.as_view(), name ="search"),
	path('store/', views.ProductView.as_view(), name ="store"),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name = "product_detail"),
	path('review/<int:pk>/', views.AddReview.as_view(), name = "add_review"),
	path('', views.index, name = "index"),
	#path('admin/', admin.site.urls),

#

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
