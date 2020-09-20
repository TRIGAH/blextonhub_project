from django.urls import path
from django.conf.urls import url
from .views import  about, contact, page_404,checkout


app_name='pages'
urlpatterns = [

    # url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^404/$', page_404, name='404'),
    
   
]