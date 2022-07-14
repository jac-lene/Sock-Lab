from statistics import mode
from xmlrpc.client import boolean
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