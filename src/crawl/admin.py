from django.contrib import admin
from . import models

admin.site.site_header = "MenuPlzzz Admin"
admin.site.site_title = "MenuPlzzz Admin"
admin.site.index_title = "Welcome MenuPlzzz Admin"

@admin.register(models.StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_date',
        'updated_date'
    )


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'storetype',
        'created_date',
        'updated_date'
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'store',
        'created_date',
        'updated_date'
    )


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_event',
        'price',
        'event_price',
        'image',
        'is_selling',
        'category',
        'store',
        'created_date',
        'updated_date'
    )