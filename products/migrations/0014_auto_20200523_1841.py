# Generated by Django 3.0.5 on 2020-05-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200523_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlaptop',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='productphone',
            name='is_active',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
