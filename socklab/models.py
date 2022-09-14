from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BasicSock(models.Model):
    name = models.CharField(max_length=100, default='My Sock Design')
    toeColor = models.CharField(max_length=100, default = 'white')
    ankleColor = models.CharField(max_length=100, default = 'white', blank=True)
    heelColor = models.CharField(max_length=100, default = 'white', blank=True)
    footColor = models.CharField(max_length=100, default = 'white', blank=True)
    ribColor = models.CharField(max_length=100, default = 'white', blank=True)
    foot_stripe = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    knitStatus = models.CharField(max_length=100, default='', blank=True)
    user_photo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stash(models.Model):
    brand = models.CharField(max_length=400, default='Brand', blank=True)
    colorName = models.CharField(max_length=400, default='white', blank=True)
    colorCode = models.CharField(max_length=100, default='#fff')
    yardage = models.CharField(max_length=100, blank=True)
    grams = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.colorName

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name