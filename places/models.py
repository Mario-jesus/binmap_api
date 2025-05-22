# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model
import uuid


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    image = models.ImageField(upload_to='places/images', null=True, blank=True)
    video = models.FileField(upload_to='places/videos', null=True, blank=True)
    is_visited = models.BooleanField(default=False)
    visited_date = models.DateField(null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ('place', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"
