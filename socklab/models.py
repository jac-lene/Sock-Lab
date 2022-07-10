from statistics import mode
from xmlrpc.client import boolean
from django.db import models

# Create your models here.

class BasicSock(models.Model):
    name = models.CharField(max_length=100, default='My Sock Design')
    CC1 = models.CharField(max_length=100, default = 'white')
    CC2 = models.CharField(max_length=100, default = 'yellow', blank=True)
    CC3 = models.CharField(max_length=100, default = 'red', blank=True)
    ankle_height = models.CharField(max_length=100, default = 'crew')
    foot_length = models.CharField(max_length=100, default = '9.5')
    foot_stripe = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    user_photo = models.TextField(default = 'upload photo here')

    def __str__(self):
        return self.name