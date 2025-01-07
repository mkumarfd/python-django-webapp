from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.Customer, CustomerAdmin)
