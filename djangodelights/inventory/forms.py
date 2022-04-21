from curses import meta
from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemAddFrom(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuRecipeAddForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'

class PurchaseAddForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'