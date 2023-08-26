from django.db import models
from django import forms


class karbar (models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    linkclass = models.CharField(max_length=150)
    phone = models.IntegerField()
    cm = models.CharField(max_length=150)
    profile = models.ImageField(
        upload_to='pictures/', default='pictures/default.png')



class homework(models.Model):
    cm = models.CharField(max_length=1500)
    file = models.FileField(upload_to='homeworks/')
