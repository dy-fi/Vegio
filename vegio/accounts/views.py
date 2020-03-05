from django.shortcuts import render
from django.views.generic.edit import CreateView


class SignupView(CreateView):
    form_class = 'django.auth.forms.UserCreationForm'
    template_name = 'registration/signup.html'