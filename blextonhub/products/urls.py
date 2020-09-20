from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.food_page, name='food'),
    path('fashion/', views.fashion_page, name='fashion'),
    path('skincare/', views.skincare_page, name='skincare'),
]