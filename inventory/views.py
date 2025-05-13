from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Inventory
from .serializers import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.select_related('ingredient').all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
