from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from ledger.models import Ingredient, Recipe, RecipeIngredient
from django.views.generic import ListView, DetailView

class RecipeBookView(ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'recipes'
    
class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'recipe'
    redirect_field_name = '/ledger/recipes/list'

def index(request):
    return HttpResponse('Hello World! This came from the index view')
