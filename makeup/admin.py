from django.contrib import admin

from .models import Prodect,Clint,Order,OrderedProduct 
admin.site.register(Prodect)
admin.site.register(Clint)
admin.site.register(Order)
admin.site.register(OrderedProduct)
