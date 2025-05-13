from rest_framework import serializers
from .models import DailyUsage
from ingredients.models import Ingredient

class IngredientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']

class DailyUsageSerializer(serializers.ModelSerializer):
    ingredient_detail = IngredientNameSerializer(source='ingredient', read_only=True)

    class Meta:
        model = DailyUsage
        fields = ['id', 'date', 'ingredient', 'ingredient_detail', 'quantity_used']
