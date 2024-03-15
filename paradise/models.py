from django.db import models
from cloudinary.models import CloudinaryField

class Merch(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default='')
    image = CloudinaryField('image', default='placeholder')
    
    def __str__(self):
        return self.name

    