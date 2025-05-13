from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime

from .models import DailyReport
from .serializers import DailyReportSerializer
from .utils import render_to_pdf  # Make sure you have this utility

class DailyReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DailyReport.objects.all().order_by('-date')
    serializer_class = DailyReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='monthly')
    def monthly_report(self, request):
        month = request.query_params.get('month')  # format: '2025-05'
        if not month:
            return Response({'error': 'month parameter is required'}, status=400)
        try:
            year, month_num = map(int, month.split('-'))
        except:
            return Response({'error': 'Invalid month format. Use YYYY-MM'}, status=400)

        reports = DailyReport.objects.filter(date__year=year, date__month=month_num)
        summary = reports.aggregate(
            total_cups=Sum('total_cups'),
            total_income=Sum('total_income'),
            total_expense=Sum('total_expense'),
            profit=Sum('profit'),
        )
        summary['month'] = month
        return Response(summary)

    @action(detail=False, methods=['get'], url_path='yearly')
    def yearly_report(self, request):
        year = request.query_params.get('year')  # format: '2025'
        if not year:
            return Response({'error': 'year parameter is required'}, status=400)

        try:
            year = int(year)
        except:
            return Response({'error': 'Invalid year format. Use YYYY'}, status=400)

        reports = DailyReport.objects.filter(date__year=year)
        summary = reports.aggregate(
            total_cups=Sum('total_cups'),
            total_income=Sum('total_income'),
            total_expense=Sum('total_expense'),
            profit=Sum('profit'),
        )
        summary['year'] = year
        return Response(summary)

    @action(detail=True, methods=['get'], url_path='pdf')
    def download_pdf(self, request, pk=None):
        report = self.get_object()
        pdf_data = render_to_pdf('reports/daily_report.html', {'report': report})
        if pdf_data:
            response = HttpResponse(pdf_data, content_type='application/pdf')
            filename = f"Daily_Report_{report.date}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        return Response({'error': 'PDF generation failed'}, status=500)

