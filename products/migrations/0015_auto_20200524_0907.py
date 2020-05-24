# Generated by Django 3.0.5 on 2020-05-24 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200523_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productlaptop',
            options={'verbose_name': 'Ноутбук', 'verbose_name_plural': 'Ноутбуки'},
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productimage', to='products.Product'),
        ),
    ]
