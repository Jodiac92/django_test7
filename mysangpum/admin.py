from django.contrib import admin
from mysangpum.models import Product, Maker

# Register your models here.
class MakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'mname', 'tel', 'addr')
admin.site.register(Maker, MakerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'price', 'maker_name')
admin.site.register(Product, ProductAdmin)