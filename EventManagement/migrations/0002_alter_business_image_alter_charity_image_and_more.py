# Generated by Django 4.1.4 on 2022-12-31 22:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='family',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='media'),
        ),
    ]