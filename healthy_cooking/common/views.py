from django.shortcuts import render
from healthy_cooking.common.models import Category


# Create your views here.
def home(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'common/home.html',  {'categories': categories})
