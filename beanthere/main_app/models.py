from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    lighting = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)
    airconditioning = models.BooleanField()
    patio = models.BooleanField()
    pet_friendly = models.BooleanField()
    traffic = models.CharField(max_length=50)
    food = models.BooleanField()
    drinks = models.BooleanField()
    wifi = models.BooleanField()
    outlets = models.BooleanField()
    comments = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
