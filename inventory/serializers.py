from rest_framework import serializers
from .models import Inventory
from ingredients.models import Ingredient

class IngredientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']

class InventorySerializer(serializers.ModelSerializer):
    ingredient_detail = IngredientNameSerializer(source='ingredient', read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'ingredient', 'ingredient_detail', 'quantity_available']
