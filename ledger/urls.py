from django.urls import path
from .views import RecipeBookView, RecipeView

app_name = "ledger"

urlpatterns = [
    path('recipes/list', RecipeBookView.as_view(), name="recipe-book"),
    path('recipes/ledger/recipe/<int:pk>', RecipeView.as_view(), name="recipe"),
]
