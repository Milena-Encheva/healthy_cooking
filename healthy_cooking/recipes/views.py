from django.urls import reverse_lazy, reverse
from django.views import generic as view
from django.shortcuts import get_object_or_404
from healthy_cooking.common.models import Category
from healthy_cooking.recipes.models import Recipe
from healthy_cooking.recipes.forms import RecipeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeCreateView(view.CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/add_recipe.html'

    def get_success_url(self):
        return reverse("recipe_detail", kwargs={
            "pk": self.object.pk,
        })

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeDetailView(view.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_details.html'
    slug_url_kwarg = 'recipe_slug'


class RecipesByCategoryListView(view.ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.kwargs.get('category_name')  # Get the category from the URL parameters
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all categories to the context
        context['categories'] = Category.objects.all()
        return context

