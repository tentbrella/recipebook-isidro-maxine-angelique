from django.urls import path

from .views import index, recipe_book, recipe1, recipe2

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_book, name="recipe-book"),
    path('recipe/1', recipe1, name="recipe1"),
    path('recipe/2', recipe2, name="recipe2"),
]

app_name = "ledger"
