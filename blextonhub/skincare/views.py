from django.shortcuts import render

# Create your views here.
def skincare_page(request):
    return render(request,'skincare/skincare.html')