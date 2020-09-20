"""blextonhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf.urls import url,include
from django.contrib import admin
from fashion.views import fashion_page
from food.views import food_page
from carts.views import cart_home, update_cart
from skincare.views import skincare_page
from pages.views import about,contact,page_404,checkout
from django.views.generic import TemplateView
from .views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name='home'),
    url(r'^food/',include('food.urls', namespace='food')),
    url(r'^fashion/',include('fashion.urls', namespace='fashion')),
    url(r'^skincare/',include('skincare.urls', namespace='skincare')),
    url(r'^index/',include('pages.urls', namespace='pages')),
    url(r'^cart/',include('carts.urls', namespace='cart')),
    
]

if settings.DEBUG:
   urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
