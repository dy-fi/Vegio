from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class SignupView(CreateView):
    form_class = 'django.auth.forms.UserCreationForm'
    template_name = 'registration/signup.html'

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("recipes:index")) 