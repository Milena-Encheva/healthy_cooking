from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("healthy_cooking.common.urls")),
    path("accounts/", include('healthy_cooking.accounts.urls')),
]
