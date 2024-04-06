from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from healthy_cooking.common.models import Category

UserModel = get_user_model()


class Rating(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'recipe')


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 50
    MAX_INSTRUCTION_LENGTH = 1000
    MAX_INGREDIENTS_LENGTH = 200

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    ingredients = models.TextField(MAX_INGREDIENTS_LENGTH)
    instructions = models.TextField(MAX_INSTRUCTION_LENGTH)
    photo = models.ImageField(upload_to='recipes_photos/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    slug = models.SlugField(unique=True, blank=True, null=False)

    def save(self, *args, **kwargs):
        # Generate the slug from the title
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def average_rating(self):
        return self.ratings.aggregate(models.Avg('rating'))['rating__avg']