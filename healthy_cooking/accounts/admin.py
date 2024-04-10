from django.contrib import admin
from .models import CookingUser, Profile


@admin.register(CookingUser)
class CookingUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email',)
    verbose_name_plural = 'Cooking Users'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'profile_picture')
    search_fields = ('user__email', 'first_name', 'last_name', 'about')
    verbose_name_plural = 'Profiles'

