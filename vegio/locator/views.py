from django.shortcuts import render
from django.views import generic

# Create your views here.
def Index(request):
    return render(request, 'locator/index.html', {})

class ListRestaurant(generic.ListView):
    template_name = 'locator/list.html'
    context_object_name = 'relevant restaurants'

    def get_queryset(self):
        """
        Return restaurants at relevant location
        """





# GLOBALS
api_url = 