from django.urls import reverse_lazy, reverse
from django.views import generic as view
from healthy_cooking.common.models import Category
from healthy_cooking.recipes.models import Recipe, Rating
from healthy_cooking.recipes.forms import RecipeCreateForm, RatingForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

UserModel = get_user_model()


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


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, view.UpdateView):
    model = Recipe
    form_class = RecipeCreateForm  # Use the same form for updating
    template_name = 'recipes/edit_recipe.html'  # Path to your HTML template

    def get_success_url(self):
        # Redirect to the recipe's detail view after a successful update
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        # Ensure that only the user who created the recipe can edit it
        recipe = self.get_object()
        return self.request.user == recipe.user

    def form_valid(self, form):
        # Optional: Add any additional processing here
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, view.DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')  # Redirect to recipe list view or your preferred view

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

class RecipeDetailView(view.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating_form'] = RatingForm()  # Add the form to the context
        return context


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
        context['categories'] = Category.objects.all()
        return context


@login_required
def rate_recipe(request, pk):
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        recipe = get_object_or_404(Recipe, pk=pk)
        Rating.objects.create(user=request.user, recipe=recipe, rating=rating_value)
        # Redirect the user back to the recipe details page
        return HttpResponseRedirect(reverse('recipe_detail', kwargs={'pk': pk}))
    return JsonResponse({'success': False})