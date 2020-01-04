
from django.urls import path

from .views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('cart', cart, name='cart'),
    path('category', category, name='category'),
    path('checkout', checkout, name='checkout'),
    path('product', product, name='product'),
    path('contact', contact, name='contact')
]
