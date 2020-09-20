from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'pages/about.html')
def contact(request):
    return render(request,'pages/contact.html')
def checkout(request):
    return render(request,'pages/checkout-complete.html')
def page_404(request):
    return render(request,'pages/404.html')
