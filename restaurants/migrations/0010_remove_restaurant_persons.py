# Generated by Django 4.1.1 on 2022-11-05 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='persons',
        ),
    ]
