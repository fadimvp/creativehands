# Generated by Django 3.2.4 on 2021-07-03 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=255)),
                ('CATDesc', models.TextField()),
                ('slug', models.SlugField()),
                ('CATImg', models.ImageField(upload_to='Category/')),
                ('CATParent', models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categoryios',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=75)),
                ('PRDVandor_Name', models.CharField(max_length=75)),
                ('PRDIMG', models.ImageField(blank=True, null=True, upload_to='')),
                ('PRDDec', models.TextField(max_length=500)),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDDisc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDSlug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('PRDCreated', models.DateTimeField()),
                ('PRDISNew', models.BooleanField(default=False)),
                ('PRDISbest', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=0)),
                ('tax', models.DecimalField(decimal_places=2, default=0.05, max_digits=2)),
                ('on_sale', models.BooleanField(default=False)),
                ('sale_date', models.BooleanField(default=True)),
                ('on_sale_start', models.DateField(blank=True, null=True)),
                ('on_sale_ends', models.DateField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('limited_products', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('weight', models.IntegerField(default=0, null=True)),
                ('length', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('width', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('PRDBrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand')),
                ('PRDCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100)),
                ('variation_vale', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            managers=[
                ('object_varations', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Product_Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDImg', models.ImageField(upload_to=product.models.image_upoad_to)),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACAlternative', models.ManyToManyField(related_name='PACAlternative', to='product.Product')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PACCProduct', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product')),
                ('PLNAlternative', models.ManyToManyField(related_name='alternative_products', to='product.Product')),
            ],
        ),
    ]
