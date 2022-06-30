from django.contrib import admin
from .models import *


@admin.register(Sneakers)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price')
    # list_editable = ('title', 'brand', 'price')


@admin.register(SizesSneakers)
class SizeSneakersAdmin(admin.ModelAdmin):
    list_display = ('size_34', 'size_35', 'size_36', 'size_37', 'size_38',
                    'size_39', 'size_40', 'size_41', 'size_42', 'size_43', 'size_44',
                    'size_45', 'size_46')
    # list_display = ('sneaker', 'size_34', 'size_35', 'size_36', 'size_37', 'size_38',
    #                 'size_39', 'size_40', 'size_41', 'size_42', 'size_43', 'size_44',
    #                 'size_45', 'size_46')
