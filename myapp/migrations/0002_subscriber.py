# Generated by Django 3.0.5 on 2020-05-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.EmailField(max_length=254)),
                ('NAME', models.CharField(max_length=128)),
            ],
        ),
    ]
