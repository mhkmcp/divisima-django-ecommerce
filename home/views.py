from django.shortcuts import render
from .models import *


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/index.html', context=context)


def cart(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/cart.html', context=context)


def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/category.html', context=context)


def checkout(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/checkout.html', context=context)


def product(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/product.html', context=context)


def contact(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home/contact.html', context=context)