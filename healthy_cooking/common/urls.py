from django.urls import path
from healthy_cooking.common.views import home, search_results

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_results, name='search_results'),
]
