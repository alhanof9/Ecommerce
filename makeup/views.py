from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hii")

def prodect(request):
    return render(request, 'makeup/prodect.html')
