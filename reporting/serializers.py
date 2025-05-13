from rest_framework import serializers
from .models import DailyReport

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['id', 'date', 'total_cups', 'total_income', 'total_expense', 'profit']
