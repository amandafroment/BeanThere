from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    lighting = models.IntegerField(default=3)
    sound = models.IntegerField(default=3)
    traffic = models.IntegerField(default=3)
    vegan = models.BooleanField()
    gluten_free = models.BooleanField()
    lactose_free = models.BooleanField()
    service = models.IntegerField(default=3)
    wifi = models.BooleanField()
    outlets = models.BooleanField()
    patio = models.BooleanField()
    pet_friendly = models.BooleanField()
    comments = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image_url = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

class Favourite(models.Model):
    cafe_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image_url = models.CharField(max_length=200)
    timestamp = models.DateTimeField()