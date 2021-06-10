# Generated by Django 3.2.4 on 2021-06-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDDec',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='PRDDisc',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='PRDIMG',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISbest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale_ends',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_date',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product_img',
            name='PRDImg',
            field=models.ImageField(upload_to=''),
        ),
    ]
