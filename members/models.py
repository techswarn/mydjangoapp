from django.db import models
from datetime import date

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  #email= models.CharField(default='s.swarn619@gmail.com', max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  updated_date = models.DateField(default=date.today)