from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
