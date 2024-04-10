from django.contrib import admin

from healthy_cooking.recipes.models import Recipe


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'average_rating')
    search_fields = ('title', 'user__email')
    list_filter = ('category',)
    verbose_name_plural = 'Recipes'

    def average_rating(self, obj):
        return obj.average_rating()
    average_rating.short_description = 'Average Rating'
