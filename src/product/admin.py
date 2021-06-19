from django.contrib import admin
from .models import Product,Product_Img,Category,Alternative,Product_Accessories,Varation

# Register your models here.


admin.site.register(Product)
admin.site.register(Varation)
admin.site.register(Product_Img)
admin.site.register(Category)
admin.site.register(Alternative)
admin.site.register(Product_Accessories)
