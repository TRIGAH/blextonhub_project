from django.shortcuts import render

# Create your views here.
def fashion_page(request):
    return render(request,'fashion/fashion.html')