from django.contrib import admin
from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("prodect" , views.prodect, name="prodect"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]
