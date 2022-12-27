# Generated by Django 4.1.1 on 2022-11-06 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0010_remove_restaurant_persons'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='restaurants/')),
                ('categories', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('narxi', models.IntegerField()),
                ('aloqa', models.CharField(max_length=150)),
                ('details', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
