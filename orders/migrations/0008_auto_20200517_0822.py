# Generated by Django 3.0.5 on 2020-05-17 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200517_0822'),
        ('orders', '0007_auto_20200515_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_phone',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer'),
        ),
    ]