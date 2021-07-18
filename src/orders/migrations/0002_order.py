# Generated by Django 3.2.4 on 2021-07-14 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('order_note', models.CharField(max_length=100)),
                ('total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Under_Process', 'Under_Process'), ('Completed', 'Completed'), ('Canceld', 'Canceld'), ('Rejected', 'Rejected')], default='NEW', max_length=100)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('is_order', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('update_at', models.CharField(max_length=100)),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
