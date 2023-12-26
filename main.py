from django.views.generic import TemplateView

from cart.cart import Cart
from shop.models import Product


class IndexView(TemplateView):
    template_name = 'index-2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        context['cart']=Cart(self.request)
        return context


class ErrorView(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart']=Cart(self.request)
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class GalleryView(TemplateView):
    template_name = 'gallery.html'


class WishlistView(TemplateView):
    template_name = 'wishlist.html'


class ContactsView(TemplateView):
    template_name = 'contact.html'
