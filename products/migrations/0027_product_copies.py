# Generated by Django 3.0.5 on 2020-05-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200530_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='copies',
            field=models.IntegerField(default=0),
        ),
    ]
