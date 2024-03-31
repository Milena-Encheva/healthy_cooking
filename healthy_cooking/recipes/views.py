from django.urls import reverse_lazy, reverse
from django.views import generic as view
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
    slug_url_kwarg = 'pet_slug'
