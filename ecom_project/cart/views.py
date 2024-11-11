from django.shortcuts import render,get_object_or_404
from .cart import Cart
from orbit.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.getproducts()
    quantities=cart.getquants()
    cart_totals=cart.total()
    return render(request,"cart_summary.html",{'cart_products':cart_products,'quantities':quantities,'cart_totals':cart_totals})

def cart_add(request):
    cart=Cart(request)

    if request.POST['action']=='post':
        product_id=int(request.POST['product_id'])
        product_qty=int(request.POST['product_qty'])
        product = get_object_or_404(Product,id=product_id)

        cart.add(product=product,quantity=product_qty)

        #get the length of the cart
        cart_quantity=cart.__len__()

        response=JsonResponse({'qty':cart_quantity})
        return response

def cart_delete(request):
    cart=Cart(request)

    if request.POST['action']=='post':
        product_id=int(request.POST['product_id'])

        cart.delete(product=product_id)

        response=JsonResponse({'id':product_id})
        return response
    

def cart_update(request):
    cart=Cart(request)

    if request.POST['action']=='post':
        product_id=int(request.POST['product_id'])
        product_qty=int(request.POST['product_qty'])

        cart.update(product=product_id,quantity=product_qty)

        response=JsonResponse({'qty':product_qty})
        return response