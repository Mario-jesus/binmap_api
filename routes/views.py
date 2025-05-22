# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from .models import Route, Municipality_has_Route
from .serializers import RouteSerializer, MunicipalityHasRouteSerializer


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows all users to perform read operations,
    but only allows admin users to perform write operations.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user.is_staff or request.user.is_superuser)


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and edit routes
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class MunicipalityHasRouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and edit relationships between municipalities and routes
    """
    queryset = Municipality_has_Route.objects.all()
    serializer_class = MunicipalityHasRouteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
