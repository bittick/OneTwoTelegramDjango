from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100, verbose_name='Наименование')
    brand = models.CharField(max_length=100, verbose_name='Брэнд')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    GENDERS = (
        ("M", "Men"),
        ("W", "Women"),
        ("U", "Unisex"),
    )
    gender = models.CharField(max_length=2, choices=GENDERS, verbose_name='Пол')

    def __str__(self):
        return self.title

    title.short_description = 'Наименование'


class Sneaker(Product):
    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'

    image1 = models.ImageField(upload_to='static/images', blank=False, verbose_name='Фото 1')
    image2 = models.ImageField(upload_to='static/images', blank=False, verbose_name='Фото 2')
    image3 = models.ImageField(upload_to='static/images', blank=False, verbose_name='Фото 3')
    image4 = models.ImageField(upload_to='static/images', blank=True, verbose_name='Фото 4 (необязательно)')
    image5 = models.ImageField(upload_to='static/images', blank=True, verbose_name='Фото 5 (необязательно)')
    image6 = models.ImageField(upload_to='static/images', blank=True, verbose_name='Фото 6 (необязательно)')


class SizesSneaker(models.Model):
    class Meta:
        verbose_name = 'Размеры'
        verbose_name_plural = 'Размеры'

    sneaker_id = models.OneToOneField(to=Sneaker, on_delete=models.CASCADE, related_name='sizes')
    size_350 = models.BooleanField(default=False, verbose_name='35')
    size_355 = models.BooleanField(default=False, verbose_name='35.5')
    size_360 = models.BooleanField(default=False, verbose_name='36')
    size_365 = models.BooleanField(default=False, verbose_name='36.5')
    size_370 = models.BooleanField(default=False, verbose_name='37')
    size_375 = models.BooleanField(default=False, verbose_name='37.5')
    size_380 = models.BooleanField(default=False, verbose_name='38')
    size_385 = models.BooleanField(default=False, verbose_name='38.5')
    size_390 = models.BooleanField(default=False, verbose_name='39')
    size_400 = models.BooleanField(default=False, verbose_name='40')
    size_405 = models.BooleanField(default=False, verbose_name='40.5')
    size_410 = models.BooleanField(default=False, verbose_name='41')
    size_420 = models.BooleanField(default=False, verbose_name='42')
    size_425 = models.BooleanField(default=False, verbose_name='42.5')
    size_430 = models.BooleanField(default=False, verbose_name='43')
    size_440 = models.BooleanField(default=False, verbose_name='44')
    size_445 = models.BooleanField(default=False, verbose_name='44.5')
    size_450 = models.BooleanField(default=False, verbose_name='45')
    size_460 = models.BooleanField(default=False, verbose_name='46')
    size_465 = models.BooleanField(default=False, verbose_name='45.5')

    def __str__(self):
        return ''


class OrderList(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    customer = models.CharField(max_length=128, verbose_name='ФИО клиента')
    shipping_address = models.CharField(max_length=128, verbose_name='Адрес доставки')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    is_paid = models.BooleanField(default=False, verbose_name='Оплата совершена')
    given_to_work = models.BooleanField(default=False, verbose_name='Отдано в работу')
    delivered = models.BooleanField(default=False, verbose_name='Доставлено')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Список товаров'
        verbose_name_plural = 'Список товаров'

    order_id = models.ForeignKey(to=OrderList, on_delete=models.PROTECT, related_name='order_items')
    sneaker_id = models.ForeignKey(to=Sneaker, on_delete=models.DO_NOTHING, verbose_name='Товар')
    sneaker_size = models.IntegerField(verbose_name='Размер')
    quantity = models.IntegerField(verbose_name='Количество')
