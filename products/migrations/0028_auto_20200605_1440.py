# Generated by Django 3.0.5 on 2020-06-05 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_product_copies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='slug',
        ),
    ]
