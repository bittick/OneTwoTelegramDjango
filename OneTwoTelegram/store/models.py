from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Products(models.Model):
    class Meta:
        abstract = True
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    GENDERS = (
        ("M", "Men"),
        ("W", "Women"),
        ("U", "Unisex"),
    )
    gender = models.CharField(max_length=2, choices=GENDERS)

    def __str__(self):
        return self.title


class Sneakers(Products):
    sneaker_sizes = models.JSONField(default={str(i): 0 for i in range(34, 46)})
    image1 = models.ImageField(upload_to='images', blank=False)
    image2 = models.ImageField(upload_to='images', blank=False, null=True)
    image3 = models.ImageField(upload_to='images', blank=False, null=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
    image6 = models.ImageField(upload_to='images', blank=True)






