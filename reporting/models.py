from django.db import models

# Create your models here.

from django.db import models

class DailyReport(models.Model):
    date = models.DateField(unique=True)
    total_cups = models.PositiveIntegerField()
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} | Cups: {self.total_cups} | Profit: {self.profit}"
