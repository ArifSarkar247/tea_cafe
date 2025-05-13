from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import DailyUsage
from .serializers import DailyUsageSerializer

class DailyUsageViewSet(viewsets.ModelViewSet):
    queryset = DailyUsage.objects.select_related('ingredient').order_by('-date')
    serializer_class = DailyUsageSerializer
    permission_classes = [permissions.IsAuthenticated]
