from django.shortcuts import render, get_object_or_404

from cart import cart
from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Category, Product


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {cart}
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'single-product.html', {'product': product, 'cart_product_form': cart_product_form})

