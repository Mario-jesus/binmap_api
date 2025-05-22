# -*- coding: utf-8 -*-
from django.db import models
import uuid

class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.TimeField()

    def __str__(self):
        return self.name


class Municipality_has_Route(models.Model):
    municipality = models.ForeignKey('places.Municipality', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('municipality', 'route')
        verbose_name = "Ruta Municipal"
        verbose_name_plural = "Rutas Municipales"

    def __str__(self):
        return f"{self.municipality.name} - {self.route.name}"
