from django import forms
from healthy_cooking.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'photo', 'category']
        widgets = {
            'instructions': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class RecipeCreateForm(RecipeBaseForm):
    pass
