from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
# Create your models here.
class Team(models.Model):
    """docstring for Team"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    role = models.CharField(max_length=30)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)