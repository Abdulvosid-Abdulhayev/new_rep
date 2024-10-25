from django.db import models

class FoodType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Food Type')

    def __str__(self):
        return self.name

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    view_count = models.IntegerField(default=0)

    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def __str__(self):
        return self.name
