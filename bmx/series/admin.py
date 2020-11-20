from django.contrib import admin

# Register your models here.

from .models import Udi, Dollar


site = admin.site

class UdiAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'value')

site.register(Udi, UdiAdmin)

class DollarAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'value')

site.register(Dollar, DollarAdmin)
