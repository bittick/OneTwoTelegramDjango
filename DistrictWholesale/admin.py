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
    list_display = ('title', 'price','product_cat')

    def get_images(self, obj):
        html_images = f'''<img src={obj.image1.url} height="100">'''
        return mark_safe(html_images)

    readonly_fields = ('get_images',)
    get_images.short_description = 'Фото'
    list_editable = ('product_cat', )


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    
    def get_phone_number(self, obj):
        return obj.customer.phone_number

    def get_total_cost(self, obj):
        items = OrderItem.objects.filter(order_id=obj.id)
        total_cost = 0
        for item in items:
            if item.product_id.weight == 'G':
                total_cost += item.quantity * item.product_id.price / 100
            else:
                total_cost += item.quantity * item.product_id.price
        return total_cost

    get_phone_number.short_description = 'Номер телефона клиента'
    get_total_cost.short_description = 'Стоимость заказа'

    fields = ('customer', 'get_phone_number', 'comment' , 'shipping_address', 'is_paid','delivery_required' , 'is_delivered','registration_date', 'edit_date', 'get_total_cost')
    list_display = ('registration_date', 'customer', 'is_paid', 'is_delivered', 'delivery_required', 'get_phone_number')
    search_fields = ('customer', )
    readonly_fields = ('registration_date', 'edit_date', 'get_phone_number', 'get_total_cost')
    inlines = [
        OrderItemInline,
    ]
    list_filter = ('is_delivered', 'delivery_required','is_paid', 'registration_date')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('name', 'telegram_id', 'phone_number', 'discount')
    list_display = ('name', 'telegram_id', 'phone_number', 'discount')
    search_fields = ('name', )


@admin.register(Category)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('title', )
    list_display = ('title', )
