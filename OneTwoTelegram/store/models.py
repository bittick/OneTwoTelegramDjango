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

    def __str__(self):
        return self.title


class Sneakers(Products):
    pass


class SizesSneakers(models.Model):
    sneaker = models.OneToOneField('Sneakers', on_delete=models.CASCADE)
    # sizes = models.PositiveSmallIntegerField(
    #     validators=[MinValueValidator(34), MaxValueValidator(45)])
    size_34 = models.IntegerField(default=0)
    size_35 = models.IntegerField(default=0)
    size_36 = models.IntegerField(default=0)
    size_37 = models.IntegerField(default=0)
    size_38 = models.IntegerField(default=0)
    size_39 = models.IntegerField(default=0)
    size_40 = models.IntegerField(default=0)
    size_41 = models.IntegerField(default=0)
    size_42 = models.IntegerField(default=0)
    size_43 = models.IntegerField(default=0)
    size_44 = models.IntegerField(default=0)
    size_45 = models.IntegerField(default=0)
    size_46 = models.IntegerField(default=0)






