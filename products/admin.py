from django.contrib import admin
from.models import Product
from.models import Offer
class ProductAdmin(admin.ModelAdmin):
   list_display= ("Name", "Price" ,"Stock","Image")
 
class OfferAdmin(admin.ModelAdmin):
     
 list_display=("code","discount")




# Register your models here. 
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)

  