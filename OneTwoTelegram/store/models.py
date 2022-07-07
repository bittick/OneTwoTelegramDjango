from django.db import models


class Product(models.Model):
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


class Sneaker(Product):
    sneaker_sizes = models.JSONField(default=get_default_sizes)
    image1 = models.ImageField(upload_to='images', blank=False)
    image2 = models.ImageField(upload_to='images', blank=False)
    image3 = models.ImageField(upload_to='images', blank=False)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
    image6 = models.ImageField(upload_to='images', blank=True)


class OrderItem(models.Model):
    product = models.ForeignKey(to=Sneaker, on_delete=models.DO_NOTHING)
    size = models.IntegerField(blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.product} размер: {self.size} х{self.quantity} '


class OrderList(models.Model):
    items = models.ManyToManyField(to=OrderItem)
    customer = models.CharField(max_length=128)
    shipping_address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    registration_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    given_to_work = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
