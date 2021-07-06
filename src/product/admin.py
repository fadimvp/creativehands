from django.contrib import admin
from .models import Product, Product_Img, Category,Variation, Alternative, Product_Accessories


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('CATName',)}
    list_display = ('CATName', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc", "PRDCost", "stock", "PRDCreated", "PRDIMG")
    list_display_links = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc",)
    search_fields = ("PRDName", "user")
    list_editable = ('stock',)




admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
admin.site.register(Product_Img)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alternative)
admin.site.register(Product_Accessories)
