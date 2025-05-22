# -*- coding: utf-8 -*-
from rest_framework import serializers
from places.serializers import MunicipalitySerializer, PlaceSerializer
from .models import Route, Municipality_has_Route


class RouteSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(read_only=True, many=True)

    class Meta:
        model = Route
        fields = ('id', 'name', 'description', 'duration', 'places', 'municipalities')

    class NestedMunicipalityHasRouteSerializer(serializers.ModelSerializer):
        municipality = MunicipalitySerializer(read_only=True)

        class Meta:
            model = Municipality_has_Route
            fields = ('municipality')

    municipalities = NestedMunicipalityHasRouteSerializer(read_only=True, many=True)


class MunicipalityHasRouteSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    municipality = MunicipalitySerializer(read_only=True)

    class Meta:
        model = Municipality_has_Route
        fields = ('route', 'municipality')
