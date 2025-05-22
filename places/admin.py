# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import State, Municipality, Category, Place


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'municipality', 'category', 'route')


admin.site.register(State, StateAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
