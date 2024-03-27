from django.urls import path
from healthy_cooking.common.views import home


urlpatterns = [
    path('', home, name='home'),
]
