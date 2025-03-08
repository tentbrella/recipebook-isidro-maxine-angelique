from django.shortcuts import render
from django.http import HttpResponse
from ledger.models import Ingredient, Recipe, RecipeIngredient
from django.views.generic import ListView, DetailView

class RecipeBookView(ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'recipes'
    
class RecipeView(DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'recipe'

def index(request):
    return HttpResponse('Hello World! This came from the index view')
