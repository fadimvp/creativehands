# Generated by Django 3.2.4 on 2021-06-19 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qty',
            new_name='stock',
        ),
    ]
