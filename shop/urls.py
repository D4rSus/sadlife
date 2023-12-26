from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('single/<int:id>/<slug:slug>/', views.product_details,
         name='product_detail'),
]