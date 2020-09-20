from django.shortcuts import render
from .models import Food
from carts.models import Cart
from django.views.generic import ListView,DetailView
# Create your views here.
def food_page(request):
    food = Food.objects.all()
    context = {
       'food':food,
       
       
      
    }
    return render(request,'food/food.html',context)


class FoodDetailView(DetailView):
    queryset = Food.objects.all()
    template_name = 'food/food.html'
    def get_context_data(self, *args, **kwargs):
         context = super(FoodDetailView, self).get_context_data(*args, **kwargs)
         cart_obj, new_obj = Cart.objects.new_or_get(self.request)
         context['cart'] = cart_obj
         return context

# class FoodListView(ListView):
#     template_name = 'food/food.html'

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return Food.objects.all()