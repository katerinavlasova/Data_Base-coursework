# Generated by Django 3.0.5 on 2020-06-05 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200605_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.Order'),
        ),
    ]
