from .models import Advertisements
from django.contrib import admin


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'created_date', 'update_date', 'auction', 'image']
    list_filter = ['auction', 'created_ad']


admin.site.register(Advertisements, AdvertisementsAdmin)
