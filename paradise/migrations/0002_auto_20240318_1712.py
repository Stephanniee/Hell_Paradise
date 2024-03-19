# Generated by Django 5.0.3 on 2024-03-18 17:12

from django.db import migrations, models
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(default='')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(default='', on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default='', on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]