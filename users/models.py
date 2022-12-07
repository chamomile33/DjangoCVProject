from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    pass

class CSVModel (models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    education = models.TextField(null=True)
    experience = models.TextField(null=True)
    skills = models.TextField(null=True)
    additional = models.TextField(null=True)
    author = models.ForeignKey('User',on_delete=models.CASCADE)

    


