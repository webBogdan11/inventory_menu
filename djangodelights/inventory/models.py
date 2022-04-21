from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/ingredients/"
    
    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menu/"
    
    def __str__(self):
        return f"title={self.title}; price={self.price}"

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menu/"

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return "/purchases/"

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"

    