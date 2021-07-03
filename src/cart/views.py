from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from product.models import Product
from .models import Cart, CartItems
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def _cart_id(request):  # creat session id to cart
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()  # create new session
    return cart


def add_cart(request, product_id):  # get product.id to  url
    if request.method == 'POST' or None:
        color = request.POST['color']
        size = request.POST['size']
        print(color, size)

    product = Product.objects.get(id=product_id)  # get the  product id one product add to cart

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # get the  cart using the cart_id present  in the session
        product = Product.objects.get(id=product_id)

        product.stock -= 1
        if product.stock == -1:
            return redirect('cart:cart_item')

        product.save()

        print('cart ============= ', )
        cart.save()
    except Cart.DoesNotExist:

        cart = Cart.objects.create(cart_id=_cart_id(request))
        print('cart v2 ============= ', cart)

        product = Product.objects.get(id=product_id)
        print('product ============= ', product)

        # create cart same id session
    cart.save()  # save objects to database
    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        print('cart_item b ============= ', cart_item.product.stock - 1)

        cart_item.quantity += 1

        product = Product.objects.get(id=product_id)

        if str(product.stock == -1):

            if product.stock <= -1:
                return redirect('cart:cart_item')

            product.save()

        product.save()
        print("save", product.stock)

        cart_item.save()






    except CartItems.DoesNotExist:  # get all data from models and save all  class CartItems

        cart_item = CartItems.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('cart:cart_item')


# remove one item inside cart
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)
    cart_item.quantity -= 1


    print('bef', cart_item.quantity)
    print('befee', cart_item.quantity)
    product = Product.objects.get(id=product_id)
    product.stock += 1
    cart_item.save()
    print('aft stock', cart_item.quantity)

    product.save()
    if cart_item.quantity < 1:



        cart_item.delete()
    return redirect('cart:cart_item')


def remove_cart_item(request, product_id):  # remove all items in related one product
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)

    cart_item.delete()
    return redirect('cart:cart_item')


def CartView(request, total=0, quantity=0, tax=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItems.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.PRDPrice * cart_item.quantity)
            quantity += cart_item.quantity
            tax += (total) * (cart_item.product.tax)
        total_tex = (total + tax)

    except ObjectDoesNotExist:
        total_tex = (total + tax)

    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax': tax,
        'total_tex': total_tex,

    }
    return render(request, 'cart.html', context)
