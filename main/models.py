from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your models here.


class details(models.Model):
    lat = models.CharField(max_length=200,default='')
    long = models.CharField(max_length=200,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="",null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, default="male")
    blood_type = models.CharField(max_length=3)
    mobile = models.BigIntegerField()
    hospital = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
