from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Prodect

from makeup.models import Prodect

def index(request):
    return HttpResponse("hii")

def prodect(request):
    return render(request, 'makeup/prodect.html',{"prodect": Prodect.objects.all()})

def product_detail(request, product_id):
    product = get_object_or_404(Prodect, id=product_id)
    return render(request, 'makeup/product_detail.html', {'product': product})