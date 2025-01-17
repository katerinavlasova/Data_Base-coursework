# Generated by Django 3.0.5 on 2020-05-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_productinorder_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
