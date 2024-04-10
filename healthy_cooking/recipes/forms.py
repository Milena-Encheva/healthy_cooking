from django import forms
from healthy_cooking.recipes.models import Recipe
from django.forms import ClearableFileInput


class CustomURLInput(forms.URLInput):
    pass


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'photo', 'category']
        widgets = {
            'instructions': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'photo': ClearableFileInput(attrs={'accept': 'image/*'})
        }

        labels = {
            'instructions': 'Instructions',
            'ingredients': 'Ingredients',
        }


class RecipeCreateForm(RecipeBaseForm):
    pass


class RatingForm(forms.Form):
    RATING_CHOICES = [
        (1, 'Bland'),
        (2, 'Okay'),
        (3, 'Tasty'),
        (4, 'Delicious'),
        (5, 'Exquisite')
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'rating-radio'}), label='')

