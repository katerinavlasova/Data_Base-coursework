# Generated by Django 3.0.5 on 2020-06-04 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_product_copies'),
        ('myapp', '0013_auto_20200604_2245'),
        ('orders', '0016_auto_20200517_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='myapp.Customer'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productinorder', to='products.Product'),
        ),
    ]
