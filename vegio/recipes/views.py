from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import requests
import json 

from recipes.recipe import get_food_recipe
from recipes.forms import RecipeForm

def Index(request):
    '''
    Returns index page with food query form
    '''
    form = RecipeForm()
    return render(request, 'recipes/index.html', {'form': form})

def ListView(request):
    '''
    Lists food query results
    '''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            foods = get_food_recipe(name)
            return render(request, 'recipes/list.html', {'food_list': foods})

    form = RecipeForm()
    return HttpResponseRedirect(reverse('recipes:index', args=(form,)))





