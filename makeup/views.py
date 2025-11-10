from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Prodect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout 

from makeup.models import Prodect

def index(request):
    return render(request,"makeup/home.html")  

def prodect(request):
    return render(request, 'makeup/prodect.html',{"prodect": Prodect.objects.all()})

def product_detail(request, product_id):
    product = get_object_or_404(Prodect, id=product_id)
    return render(request, 'makeup/product_detail.html', {'product': product})

def register(request):                               
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # show login page after creating the account
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "makeup/register.html", {"form": form})

def login_view(request):                             
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")    # go to home after login
    else:
        form = AuthenticationForm()
    return render(request, "makeup/login.html", {"form": form})

def logout_view(request):                            
    logout(request)
    return redirect("login")