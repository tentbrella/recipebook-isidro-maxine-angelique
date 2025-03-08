from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)
    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
    def __str__(self):
        return '{}: needs {} of {}'.format(self.recipe, self.quantity, self.ingredient)
