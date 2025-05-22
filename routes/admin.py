# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Route, Municipality_has_Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')


class Municipality_has_RouteAdmin(admin.ModelAdmin):
    list_display = ('municipality', 'route')

admin.site.register(Route, RouteAdmin)
admin.site.register(Municipality_has_Route, Municipality_has_RouteAdmin)
