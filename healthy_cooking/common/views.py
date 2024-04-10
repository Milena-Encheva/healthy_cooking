from django.shortcuts import render

from healthy_cooking.common.forms import SearchForm
from healthy_cooking.common.models import Category
from healthy_cooking.recipes.models import Recipe
from django.db.models import Max


def home(request):
    categories = Category.objects.all()
    # Get the recipe of the day - the one with the highest rating
    recipe_of_the_day = Recipe.objects.annotate(max_rating=Max('ratings__rating')).order_by('-max_rating').first()
    return render(request, 'common/home.html', {'categories': categories, 'recipe_of_the_day': recipe_of_the_day})


def search_results(request):
    form = SearchForm(request.GET or None)
    results = None
    search_attempted = 'query' in request.GET

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Recipe.objects.filter(title__icontains=query)

    return render(request, 'common/search_results.html', {
        'form': form,
        'results': results,
        'search_attempted': search_attempted
    })