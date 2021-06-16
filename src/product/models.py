# _*_ coding: utf-8 _*_
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.
from docutils.parsers.rst.directives.admonitions import Note

User = settings.AUTH_USER_MODEL


#
# class ProductQuerySet(models.query.QuerySet):
#     def PRDName(self):
#         return self.filter(PRDName=False)
# class ProductManger (models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model,using=self._db)
#     def all (self,*args,**kwargs):
#         return self.get_queryset().PRDName()
class Product(models.Model):
    # objects =ProductManger()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    PRDName = models.CharField(max_length=75)
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    PRDIMG = models.ImageField(upload_to='', blank=True, null=True)
    PRDDec = models.TextField(max_length=500)
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2)
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2)
    PRDDisc = models.DecimalField(max_digits=5, decimal_places=2)
    PRDSlug = models.SlugField(blank=True, null=True, allow_unicode=True)
    PRDCreated = models.DateTimeField()
    PRDISNew = models.BooleanField(default=False)
    PRDISbest = models.BooleanField(default=False)
    qty = models.IntegerField(default=0)

    # Additional data
    on_sale = models.BooleanField(default=False)
    sale_date = models.BooleanField(default=True)
    on_sale_start = models.DateField(null=True, blank=True)
    on_sale_ends = models.DateField(null=True, blank=True)

    # admin data
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    # Needs to Add Rating

    # Proprites
    weight = models.IntegerField(default=0, null=True)
    length = models.DecimalField(decimal_places=2, default=0, max_digits=100)
    height = models.DecimalField(decimal_places=2, default=0, max_digits=100)
    width = models.DecimalField(decimal_places=2, default=0, max_digits=100)

    def __str__(self):
        return str(self.PRDName)

    def save(self, *args, **kwargs):
        def save(self, *args, **kwargs):

            if not self.PRDSlug:
                self.PRDSlug = slugify(self.PRDName)

                if not self.PRDSlug:
                    self.PRDSlug = self.arabic_slugify(self.PRDName)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.PRDName

    def save(self, *args, **kwargs):

        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:pro_detail', kwargs={"slug": self.PRDSlug})


class Varation_Img(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    PRDName = models.CharField(max_length=75)

    PRDIMG = models.ImageField(upload_to='', blank=True, null=True)
    def __str__(self):
        return str(Varation_Img.PRDName)
    def get_absolute_url(self):
        return self.product.get_absolute_url()




class Product_Img(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE)

    PRDImg = models.ImageField(upload_to='')

    def __str__(self):
        return str(self.PRDImg)


class Category(models.Model):
    CATName = models.CharField(max_length=255)
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True}, on_delete=models.CASCADE,
                                  blank=True, null=True)
    CATDesc = models.TextField()
    CATImg = models.ImageField(upload_to='Category/')

    def __str__(self):
        return self.CATName


class Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product')
    PLNAlternative = models.ManyToManyField(Product, related_name='alternative_products')

    def __str__(self):
        return self.PLNAlternative


class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="PACCProduct")
    PACAlternative = models.ManyToManyField(Product, related_name="PACAlternative")

    def __str__(self):
        return str(self.PACCProduct)
