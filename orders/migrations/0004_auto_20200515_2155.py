# Generated by Django 3.0.5 on 2020-05-15 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200515_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_phone',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='number',
        ),
    ]