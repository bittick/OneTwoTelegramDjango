from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    classes = ('collapse',)


class SizesSneakerInline(admin.StackedInline):
    model = SizesSneaker
    min_num = 1
    max_num = 1
    classes = ('collapse',)

    fields = (('size_350', 'size_355', 'size_360', 'size_365'),
              ('size_370', 'size_375', 'size_380', 'size_385'),
              ('size_390', 'size_400', 'size_405', 'size_410'),
              ('size_420', 'size_425', 'size_430', 'size_440'),
              ('size_445', 'size_450', 'size_460', 'size_465'),)


@admin.register(Sneaker)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price')

    def get_images(self, obj):
        html_images = f'''<img src={obj.image1.url} height="100">''' \
                      + f'''<img src={obj.image2.url} height="100">''' \
                      + f'''<img src={obj.image3.url} height="100">'''
        if obj.image4:
            html_images += f'''<img src={obj.image4.url} height="100">'''
        if obj.image5:
            html_images += f'''<img src={obj.image4.url} height="100">'''
        if obj.image6:
            html_images += f'''<img src={obj.image4.url} height="100">'''
        return mark_safe(html_images)

    readonly_fields = ('get_images',)

    inlines = [
        SizesSneakerInline
    ]

    get_images.short_description = 'Фотографии'
    Sneaker.image1.short_description = 'Фото'


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):

    list_display = ('id', 'registration_date', 'customer', 'is_paid', 'given_to_work', 'delivered', 'phone_number')
    search_fields = ('id', 'customer')

    inlines = [
        OrderItemInline,
    ]
