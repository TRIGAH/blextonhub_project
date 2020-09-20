from django.conf.urls import url
from .views import skincare_page

app_name='skincare'
urlpatterns = [
     url(r'^$', skincare_page, name='skincare'),
]