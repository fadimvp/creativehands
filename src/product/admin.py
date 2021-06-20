from django.contrib import admin
from .models import Product, Product_Img, Category, Alternative, Product_Accessories, Varation


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('CATName',)}
    list_display = ('CATName', 'slug')


admin.site.register(Product)
admin.site.register(Varation)
admin.site.register(Product_Img)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alternative)
admin.site.register(Product_Accessories)
