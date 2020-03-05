from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from recipes.models import Recipe 

class SignupView(CreateView):
    form_class = 'django.auth.forms.UserCreationForm'
    template_name = 'registration/signup.html'

# class ListRecipes(ListView):
#     template_name = 'registration/list.html'
#     model = Recipe
#     paginate_by = 10

#     def get_queryset(self, **kwargs):
