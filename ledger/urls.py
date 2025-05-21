from django.urls import path
from .views import RecipeBookView, RecipeView

app_name = "ledger"

urlpatterns = [
    path('recipes/list', RecipeBookView.as_view(), name="recipe-book"),
    path('recipe/add', RecipeView.as_view(), name="recipe-add"),
    path('recipe/<int:pk>', RecipeView.as_view(), name="recipe"),
    path('recipe/<int:pk>/add_image', RecipeView.as_view(), name="recipe-img"),
    path('accounts/login', include('django.contrib.auth.urls')),
    path('accounts/logout', include('django.contrib.auth.urls')),
    ]
