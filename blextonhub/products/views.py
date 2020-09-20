from django.shortcuts import render

# Create your views here.
def food_page(request):
    return render(request,'products/food.html')
def fashion_page(request):
    return render(request,'products/fashion.html')
def skincare_page(request):
    return render(request,'products/skincare.html')
