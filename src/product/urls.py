from django.urls import path

from . import views
app_name ='product'
urlpatterns = [
    path('', views.Product_list, name='pro_list'),
    path('<slug:slug>', views.Product_detail, name='pro_detail'),
    path('store/<slug:category_slug>', views.store, name='category_slug'),
    path('store/', views.store, name='store'),

    path('search/', views.Product_list, name='search'),
]
