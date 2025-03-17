from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})