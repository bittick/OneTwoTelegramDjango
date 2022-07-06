from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Sneakers)
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
