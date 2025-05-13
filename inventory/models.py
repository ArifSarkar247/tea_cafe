from django.db import models

# Create your models here.

from django.db import models
from ingredients.models import Ingredient

class Inventory(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='inventory')
    quantity_available = models.DecimalField(max_digits=10, decimal_places=2)  # eg. 2.5 liters, 1.75 kg

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity_available} {self.ingredient.unit}"
