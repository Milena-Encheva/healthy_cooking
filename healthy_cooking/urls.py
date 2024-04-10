from django.contrib import admin
from django.urls import path, include
from healthy_cooking import settings
from django.conf.urls.static import static
from healthy_cooking.common.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("healthy_cooking.common.urls")),
    path("accounts/", include('healthy_cooking.accounts.urls')),
    path("recipes/", include('healthy_cooking.recipes.urls')),

]

handler404 = custom_404_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
