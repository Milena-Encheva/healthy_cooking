from healthy_cooking.recipes.views import RecipeCreateView, RecipeDetailView, RecipesByCategoryListView
from django.urls import path, include

urlpatterns = [
    path('', RecipesByCategoryListView.as_view(), name='recipe_list'),
    path('category/<str:category_name>/', RecipesByCategoryListView.as_view(), name='recipes_by_category'),
    path('add/', RecipeCreateView.as_view(), name='add recipe'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    ]
