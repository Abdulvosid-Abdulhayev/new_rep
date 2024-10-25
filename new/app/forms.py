from django import forms
from .models import Food, FoodType

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'name', 'ingredients', 'price']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'name', 'ingredients', 'price']

class FoodTypeForm(forms.ModelForm):
    class Meta:
        model = FoodType
        fields = ['name']