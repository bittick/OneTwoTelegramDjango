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

def get_default_items():
    return [
        {
            'sneaker_id': None,
            'sneaker_title' : None,
            'size' : None,
            'quantity' : None,
        }
    for i in range(3)]


class Sneaker(Product):
    sneaker_sizes = models.JSONField(default=get_default_sizes)
    image1 = models.ImageField(upload_to='images', blank=False)
    image2 = models.ImageField(upload_to='images', blank=False)
    image3 = models.ImageField(upload_to='images', blank=False)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
    image6 = models.ImageField(upload_to='images', blank=True)


class OrderList(models.Model):
    customer = models.CharField(max_length=128)
    shipping_address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    registration_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    given_to_work = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)


class OrderItem(models.Model):
    order_id = models.ForeignKey(to=OrderList, on_delete=models.PROTECT)
    sneaker_id = models.ForeignKey(to=Sneaker, on_delete=models.DO_NOTHING)
    sneaker_size = models.IntegerField()
    quantity = models.IntegerField()