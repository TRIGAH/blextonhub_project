from django.conf.urls import url
from .views import fashion_page

app_name='fashion'
urlpatterns = [
     url(r'^$', fashion_page, name='fashion'),
]