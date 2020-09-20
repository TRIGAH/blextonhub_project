from django.conf.urls import url
from .views import food_page,FoodDetailView

app_name='food'
urlpatterns = [
     url(r'^$', food_page, name='food'),
     url(r'^detail/$', FoodDetailView.as_view(), name='detail'),
]