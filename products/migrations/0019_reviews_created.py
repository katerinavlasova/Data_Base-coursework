# Generated by Django 3.0.5 on 2020-05-24 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_reviews_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]