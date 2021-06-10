from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product
from django.core.paginator import Paginator

from django.utils.translation import gettext as aa

def Product_list(request):
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
    pro_detail = get_object_or_404(Product,PRDSlug=slug)
    context = {
        'pro_detail': pro_detail,

    }
    return render(request, 'product/singlpage.html', context)


