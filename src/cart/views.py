from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from product.models import Product
from .models import Cart, CartItems
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):         # creat session id to cart
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()     # create new session
    return cart


def add_cart(request, product_id):                              # get product.id to  url
    product = Product.objects.get(id=product_id)                # get the  product id one product add to cart
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))      # get the  cart using the cart_id present  in the session
    except Cart.DoesNotExist:

        cart = Cart.objects.create(cart_id=_cart_id(request))   # create cart same id session

    cart.save()                                                 # save objects to database
    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        d = cart_item
        ST = product.stock
        b = ST - d.quantity
        s =Product.objects.create(
        PRDName = product.PRDName,
        PRDPrice=product.PRDPrice,
        PRDCost = product.PRDCost,
        PRDDisc = product.PRDDisc,
        PRDCreated = product.PRDCreated,
        stock= b,
        )

        s.save()
        cart_item.save()

    except CartItems.DoesNotExist:  # get all data from models and save all  class CartItems

        cart_item = CartItems.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    except Product.DoesNotExist:
        cart_item = Product.objects.create(
            stock=product,

        )
        cart_item.save()

    return redirect('cart:cart_item')

# remove one item inside cart
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_item')


def remove_cart_item(request, product_id):               # remove all items in related one product
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)

    cart_item.delete()
    return redirect('cart:cart_item')


def CartView(request, total=0, quantity=0, tax=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItems.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.PRDPrice * cart_item.quantity)


            quantity += cart_item.quantity

            tax += (total) * (cart_item.product.tax)
        total_tex = (total + tax)

    except ObjectDoesNotExist:
        pass

    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax': tax,
        'total_tex': total_tex,

    }
    return render(request, 'cart.html', context)
