from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    images = Recipe.objects.all()
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe, 'images': images,})

@login_required
def add_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, "ledger/add_recipe.html", {"form": form})

def add_recipe_image(request, id):
    recipe = Recipe.objects.get(id=id)
    form = RecipeImageForm()

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_detail', id=recipe.id)
            
        
    return render(request, "ledger/add_recipe_image.html", {"form": form, "recipe": recipe})

    


