from django.db import models

# Create your models here.
class Profile2(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    dob=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    linkedin=models.CharField(max_length=255)
    Qualification=models.CharField(max_length=255)
    objective=models.CharField(max_length=255)
    github=models.CharField(max_length=255)


