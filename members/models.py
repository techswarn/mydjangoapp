from django.db import models
from datetime import date

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  location = models.CharField(max_length=255, default="India")
  email = models.EmailField(max_length=255, unique=True, default=None)
  phone = models.IntegerField(null=True)
  pincode = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  updated_date = models.DateField(default=date.today)