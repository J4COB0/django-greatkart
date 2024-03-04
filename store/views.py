from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")

    product_count = products.count()

    # PAGINATOR
    paginator = Paginator(products, 3)
    page = request.GET.get("page")
    page_product = paginator.get_page(page)

    context = {
        "products": page_product,
        "product_count": product_count,
    }
    return render(request, "store/store.html", context=context)


def product_detail(request, category_slug, product_slug):
    try:
        product = get_object_or_404(
            Product, category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product).exists()
    except Exception as e:
        raise e
    context = {
        "product": product,
        "in_cart": in_cart,
    }
    return render(request, "store/product_detail.html", context=context)


def search(request):
    product_count = 0
    products = {}
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products = Product.objects.order_by(
                "-created_date").filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count,
    }

    return render(request, "store/store.html", context=context)
