from django.db import models


# Create your models here.
class Item (models.Model):
    name=models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.CharField(max_length=200, unique=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
