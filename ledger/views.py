from django.shortcuts import render
from django.http import HttpResponse
from ledger.models import Ingredient, Recipe, RecipeIngredient

def index(request):
    return HttpResponse('Hello World! This came from the index view')
def recipe_book(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": Ingredient.objects.filter(recipe__recipe__name="Recipe 1"),
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": Ingredient.objects.filter(recipe__recipe__name="Recipe 2"),  
                "link": "/recipe/2"
            }
        ]
    }
    return render(request, "list.html", ctx)
def recipe1(request):
    ctx = {
    "name": "Recipe 1",
    "ingredients": Ingredient.objects.filter(recipe__recipe__name="Recipe 1")
    "link": "/recipe/1"
    }
    return render(request, "base.html", ctx)
def recipe2(request):
    ctx = {
    "name": "Recipe 2",
    "ingredients": "ingredients": Ingredient.objects.filter(recipe__recipe__name="Recipe 2"),
        "link": "/recipe/2"
    }
    return render(request, "base.html", ctx)

