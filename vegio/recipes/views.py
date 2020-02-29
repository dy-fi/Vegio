from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import requests
import json 

from recipes.recipe import get_food_recipe
from recipes.forms import RecipeForm

# Create your views here.
def Index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            foods = get_food_recipe(name)
            HttpResponseRedirect('/recipes/list' + json.dumps(foods))
    else:
        form = RecipeForm()

    return render(request, 'recipes/index.html', {'form': form})

def ListView(request, data):
    print(request.GET)
    food_list = json.loads(data)

    return render(request, 'recipes/list.html', {'food_list': food_list})





