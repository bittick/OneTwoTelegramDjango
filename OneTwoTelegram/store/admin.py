from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class SizesSneakerInline(admin.TabularInline):
    model = SizesSneaker
    min_num = 1
    max_num = 1


@admin.register(Sneaker)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price')

    def get_images(self, obj):
        html_images = f'''<img src={obj.image1.url} height="100">'''\
                      + f'''<img src={obj.image2.url} height="100">'''\
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
    
    def get_items(self, obj):
        text = ''

        if isinstance(obj.items, list):
            for item in obj.items:
                text += f'Товар: {item["sneaker_title"]}, Размер: {item["size"]}, Количество: {item["quantity"]}\n'
        else:
            text = f'Товар: {obj.items["sneaker_title"]}, Размер: {obj.items["size"]}, Количество: {obj.items["quantity"]}'
        return text

    readonly_fields = ('get_items', )

    list_display = ('registration_date', 'customer', 'given_to_work', 'delivered', 'phone_number')

    inlines = [
        OrderItemInline,
    ]



