# Generated by Django 3.0.5 on 2020-05-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_productimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, upload_to='media/product_images/'),
        ),
    ]