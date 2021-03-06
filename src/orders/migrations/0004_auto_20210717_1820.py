# Generated by Django 3.2.4 on 2021-07-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210714_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='update_at',
        ),
        migrations.AlterField(
            model_name='order',
            name='is_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
