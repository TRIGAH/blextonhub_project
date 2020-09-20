from django.shortcuts import render, redirect
from food.models import Food
from .models import Cart
# Create your views here.
# def cart_create(request):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart Created')
#     return cart_obj


def cart_home(request):
    
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    foods = cart_obj.foods.all()
    total = 0
    for x in foods:
        total +=x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    context = {
        'object_list' : foods,
        'total':total
    }
    
    
  
    return render(request,'carts/add_to_cart.html',context) 
    # if cart_id is None:
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    #     print('New Cart Created')
    # else:
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count()==1: 
    #     print('Card ID Exists')  
    #     cart_obj = qs.first()
    #     if request.user.is_authenticated and cart_obj.user is None:
    #         cart_obj.user = request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id

def update_cart(request):
    print(request.POST)
    food_id = request.POST.get('food_id')
    if food_id is not None:
        try:
            food_obj = Food.objects.get(id=food_id)
        except Food.DoesNotExist:   
                print("It has been added")
                return redirect('page:index') 
        cart_obj, new_obj = Cart.objects.new_or_get(request)
                # return redirect(product_obj.get_absolute_url())
        if food_obj in cart_obj.foods.all():
            cart_obj.foods.remove(food_obj)
          
        else: 
            cart_obj.foods.add(food_obj)
        request.session['cart_items'] = cart_obj.foods.count()   

    return redirect('cart:home')
