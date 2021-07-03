from django.contrib import admin
from .models import Product, Product_Img, Category, Alternative, Product_Accessories, Varation


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('CATName',)}
    list_display = ('CATName', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc", "PRDCost", "stock", "PRDCreated", "PRDIMG")
    list_display_links = ("id", 'user', "PRDName", "PRDPrice", "PRDDisc",)
    search_fields = ("PRDName", "user")
    list_editable = ('stock',)


class VarationAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'variation_category','variation_vale','is_active',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Varation,VarationAdmin)
admin.site.register(Product_Img)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alternative)
admin.site.register(Product_Accessories)
