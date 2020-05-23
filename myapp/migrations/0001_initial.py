# Generated by Django 3.0.5 on 2020-04-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRAND', models.CharField(max_length=40)),
                ('OS', models.CharField(max_length=40)),
                ('SERIES', models.CharField(max_length=30)),
                ('CPU', models.CharField(max_length=40)),
                ('CORES', models.IntegerField()),
                ('MEMORY_FREQ', models.CharField(max_length=10)),
                ('RAM', models.CharField(max_length=10)),
                ('RESOLUTION', models.CharField(max_length=40)),
                ('DISPLAY_DIAGONAL', models.CharField(max_length=30)),
                ('COLOR', models.CharField(max_length=10)),
                ('WEIGHT', models.CharField(max_length=10)),
                ('COUNTRTY', models.CharField(max_length=15)),
                ('WARRANTY', models.CharField(max_length=10)),
            ],
        ),
    ]
