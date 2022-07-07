from django.db import models
from PIL import Image as Img
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


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


def get_default_sizes():
    return {str(i): 0 for i in range(34, 46)}


class Sneakers(Products):
    sneaker_sizes = models.JSONField(default=get_default_sizes)
    image1 = models.ImageField(upload_to='images', blank=False)
    image2 = models.ImageField(upload_to='images', blank=False)
    image3 = models.ImageField(upload_to='images', blank=False)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
    image6 = models.ImageField(upload_to='images', blank=True)







