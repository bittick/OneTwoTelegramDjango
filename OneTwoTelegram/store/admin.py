from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Sneaker)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price')

    def get_image(self, obj):
        return mark_safe(f'''<img src={obj.image1.url} height="100">'''
                         f'''<img src={obj.image2.url} height="100">'''
                         f'''<img src={obj.image3.url} height="100">'''
                         # f'''<img src={obj.image4.url} height="100">'''
                         # f'''<img src={obj.image5.url} height="100">'''
                         # f'''<img src={obj.image6.url} height="100">'''
                         )

    readonly_fields = ('get_image',)


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



