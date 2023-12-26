"""
URL configuration for lukas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main import IndexView, ErrorView, WishlistView, AboutView, GalleryView, ContactsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view()),
    path('404/', ErrorView.as_view()),
    path('wishlist/', WishlistView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactsView.as_view()),
    path('', include("shop.urls", namespace='shop')),
    path('orders/', include('order.urls', namespace='order')),
]
