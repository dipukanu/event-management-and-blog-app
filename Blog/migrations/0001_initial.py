# Generated by Django 4.1.4 on 2023-01-03 13:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_heading', models.CharField(max_length=200)),
                ('blog_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('blog_desc', models.TextField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('pub_name', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('comments', models.TextField(max_length=500)),
            ],
        ),
    ]
