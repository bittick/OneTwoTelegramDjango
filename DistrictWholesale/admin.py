from django.contrib import admin
from django.utils.safestring import mark_safe
from numpy import product

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    classes = ('collapse',)
    
    def get_weight(self, obj):
        if obj.product_id.weight == "UN":
            return "ШТ"
        elif obj.product_id.weight == "KG":
            return "КГ"
        else:
            return "Г"
            
    get_weight.short_description = 'Единицы измерения'
    readonly_fields = ('get_weight', )

@admin.register(Product)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

    def get_images(self, obj):
        html_images = f'''<img src={obj.image1.url} height="100">'''
        return mark_safe(html_images)

    readonly_fields = ('get_images',)
    get_images.short_description = 'Фото'


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    fields = ('customer', 'shipping_address', 'is_paid', 'registration_date', 'edit_date')
    list_display = ('registration_date', 'customer', 'is_paid')
    search_fields = ('customer', )
    readonly_fields = ('registration_date', 'edit_date')
    inlines = [
        OrderItemInline,
    ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('name', 'telegram_id', 'phone_number')
    list_display = ('name', 'telegram_id', 'phone_number')
    search_fields = ('name', )
