from django.db import models


class Category(models.Model):
    STARTERS = 'Starters'
    MAIN_DISHES = 'Main Dishes'
    DESSERTS = 'Desserts'

    CATEGORY_CHOICES = [
        (STARTERS, 'Starters'),
        (MAIN_DISHES, 'Main Dishes'),
        (DESSERTS, 'Desserts'),
    ]

    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    photo = models.URLField()

    def __str__(self):
        return self.name

