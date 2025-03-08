from django.shortcuts import render
from django.http import HttpResponse
from ledger.models import Ingredient, Recipe, RecipeIngredient
from django.views.generic import ListView, DetailView

class RecipeBookView(ListView):
    model = Recipe
    template_name = 'list.html'
    
class RecipeView(DetailView):
    model = Recipe
    template_name = 'base.html'

def index(request):
    return HttpResponse('Hello World! This came from the index view')
