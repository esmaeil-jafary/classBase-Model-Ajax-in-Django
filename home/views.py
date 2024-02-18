from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from . models import *

def home(request):
    product = Product.objects.all()
    return render(request, 'home/home.html', {'product':product})

def detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'home/detail.html', {'product':product})

def favourite_product(request, id):   
    product = get_object_or_404(Product, id=id)
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
    product.save()
    data = {'seccess': 'ok'}#برای اینکه از ایجکس استفاده کنیم باید یک دیکشنری ایجاد کنیم
    return JsonResponse(data)
