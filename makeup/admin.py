from django.contrib import admin

from .models import Prodect,Order,OrderedProduct 
admin.site.register(Prodect)
admin.site.register(Order)
admin.site.register(OrderedProduct)
