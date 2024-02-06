from django.db import models


# Create your models here.
"""
This is my model for the items that will be for giveaway in the shed .
"""
class Item (models.Model):
    name=models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.CharField(max_length=200, unique=True)
    image_alt_text = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
