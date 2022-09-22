from platform import release
from django.db import models

# Create your models here.

class Song(models.Model):
    title= models.CharField(max_length=255)
    artist= models.CharField(max_length=255)
    album= models.CharField(max_length=255)
    release= models.DateField()
    genre= models.CharField(max_length=255)