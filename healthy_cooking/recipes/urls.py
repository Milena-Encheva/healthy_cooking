from healthy_cooking.recipes.views import RecipeCreateView, RecipeDetailView
from django.urls import path, include

urlpatterns = [
    path('add/', RecipeCreateView.as_view(), name='add recipe'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    ]
