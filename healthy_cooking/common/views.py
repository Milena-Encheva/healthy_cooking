from django.shortcuts import render
from healthy_cooking.common.models import Category
from healthy_cooking.recipes.models import Recipe
from django.db.models import Max


def home(request):
    categories = Category.objects.all()
    # Get the recipe of the day - the one with the highest rating
    recipe_of_the_day = Recipe.objects.annotate(max_rating=Max('ratings__rating')).order_by('-max_rating').first()
    return render(request, 'common/home.html', {'categories': categories, 'recipe_of_the_day': recipe_of_the_day})

