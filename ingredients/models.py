from django.db import models

# Create your models here.

from django.db import models

class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('liter', 'Liter'),
        ('kg', 'Kilogram'),
        ('gram', 'Gram'),
        ('ml', 'Milliliter'),
    ]

    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.unit})"
