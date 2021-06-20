from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Product ,Category
from django.core.paginator import Paginator
from .models import Category
from django.utils.translation import gettext as aa


def Product_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        product_list = Product.objects.filter(PRDName__icontains=q)
    else:
        product_list = Product.objects.all()

    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    context = {
        'product_list': product_list,

    }
    return render(request, 'product/product_list.html', context)


def Product_detail(request, slug):
    # pro_detail = Product.objects.get(slug=slug)
    pro_detail = get_object_or_404(Product, PRDSlug=slug)
    context = {
        'pro_detail': pro_detail,

    }
    return render(request, 'product/singlpage.html', context)


def store(request,category_slug=None):
    categories = None
    product_list = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        product_list = Product.objects.filter(PRDCategory=categories, approved=True)
        product_count= product_list.count()
    else:
        product_list = Product.objects.all().filter(approved=True)
        product_count= product_list.count()

    context = {
        'product_list': product_list,
        'product_count': product_count,

    }
    return render(request, 'product/store.html', context)


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        product_list = Product.objects.filter(PRDName__icontains=q)
        print("dsdsd")
    else:
        product_list = Product.objects.all()
        print("dsd")
    context = {
        'product_list': product_list,
    }
    return render(request, 'product/product_list.html', context)
