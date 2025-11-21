from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Prodect, Clint, Order, OrderedProduct
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
            return redirect("prodect")    # go to home after login
    else:
        form = AuthenticationForm()
    return render(request, "makeup/login.html", {"form": form})

def logout_view(request):                            
    logout(request)
    return redirect("login")

def product_detail(request, product_id):
    product = get_object_or_404(Prodect, pk=product_id)

    if request.method == "POST":
        amount = request.POST.get("amount", "1")
        try:
            amount = int(amount)
        except ValueError:
            amount = 1
        if amount < 1:
            amount = 1

        basket = request.session.get("basket", {})
        pid = str(product.id)

        basket[pid] = basket.get(pid, 0) + amount

        request.session["basket"] = basket
        return redirect("basket")

    return render(request, "makeup/product_detail.html", {"product": product})


def basket(request):
    if request.method == "POST":
        if "empty" in request.POST:
            request.session["basket"] = {}
            return redirect("basket")

        if "update" in request.POST:
            basket = request.session.get("basket", {})
            new_basket = {}
            for pid, qty in basket.items():
                new_qty = request.POST.get(f"qty_{pid}", "0")
                try:
                    new_qty = int(new_qty)
                except ValueError:
                    new_qty = 0
                if new_qty > 0:
                    new_basket[pid] = new_qty

            request.session["basket"] = new_basket
            return redirect("basket")

    basket = request.session.get("basket", {})
    product_ids = basket.keys()
    products = Prodect.objects.filter(id__in=product_ids)

    items = []
    total = 0
    for p in products:
        qty = basket.get(str(p.id), 0)
        subtotal = p.price * qty
        total += subtotal
        items.append({
            "product": p,
            "qty": qty,
            "subtotal": subtotal
        })

    context = {"items": items, "total": total}
    return render(request, "makeup/basket.html", context)


def order(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    basket_data = request.session.get("basket", {}) #we could change here
    product_ids = basket_data.keys()
    products = Prodect.objects.filter(id__in=product_ids)

    items = []
    total = 0
    for p in products:
        qty = basket_data.get(str(p.id), 0)
        subtotal = p.price * qty
        total += subtotal
        items.append({
            "product": p,
            "qty": qty,
            "subtotal": subtotal
        })

    if request.method == "GET":
        data = { 
            "items" : items,
            "total" : total
        }
        return render(request, "makeup/order.html", data)    
    
    if request.method == "POST":
        if not items:
            return redirect("basket")
        
        username = request.user.username 

        clint = Clint.objects.filter(name=username).first() #we could change here
        if clint is None:
            clint = Clint(name=username, pas="")
            clint.save()
        
        order = Order(clint=clint)
        order.save()

        for item in items:
            OrderedProduct.objects.create(
                order=order,
                prodect=item["product"],
                amount=item["qty"]
            )
        
        request.session["basket"] = {}
        return render(request, "makeup/success.html", {"order": order})