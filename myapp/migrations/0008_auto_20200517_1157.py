# Generated by Django 3.0.5 on 2020-05-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200517_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='NAME',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
