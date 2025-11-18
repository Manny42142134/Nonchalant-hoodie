from django.contrib import admin
from .models import Category, Customer, Products, Order, SiteSettings

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "updated")