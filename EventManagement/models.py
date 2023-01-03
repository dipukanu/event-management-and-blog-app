from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User


#  Create your models here.
# Family:

class Family(models.Model):
    event_type = models.CharField(max_length=300)
    desc = models.TextField()
    image = CloudinaryField('media')
    food = models.CharField(max_length=200)
    decoration = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

# Charity:


class Charity(models.Model):
    event_type = models.CharField(max_length=300)
    desc = models.TextField()
    image = CloudinaryField('media')
    food = models.CharField(max_length=200)
    decoration = models.CharField(max_length=500)
    chief_guest = models.CharField(max_length=100)
    sponsor = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

# Business:


class Business(models.Model):
    event_type = models.CharField(max_length=300)
    desc = models.TextField()
    image = CloudinaryField('media')
    food = models.CharField(max_length=100)
    chief_guest = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')


# Culture:

class Culture(models.Model):
    event_type = models.CharField(max_length=300)
    desc = models.TextField()
    image = CloudinaryField('media')
    food = models.CharField(max_length=100)
    chief_guest = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')


# Book Event:

class Book_event(models.Model):
    name = models.CharField(max_length=50)
    mobile = PhoneNumberField()
    email = models.EmailField()
    location = models.CharField(max_length=500)
    people = models.IntegerField()
    date = models.DateField()
    event = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


# Contact Us:

class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    mobile = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email
