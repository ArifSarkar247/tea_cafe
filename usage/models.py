from django.db import models

# Create your models here.

from django.db import models
from ingredients.models import Ingredient

class DailyUsage(models.Model):
    date = models.DateField(auto_now_add=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('date', 'ingredient')

    def __str__(self):
        return f"{self.date} - {self.ingredient.name} - {self.quantity_used} {self.ingredient.unit}"
