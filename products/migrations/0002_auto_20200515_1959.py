# Generated by Django 3.0.5 on 2020-05-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='description',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, upload_to='media/'),
        ),
    ]
