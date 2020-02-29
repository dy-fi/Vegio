from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.Index, name='index'),
    # path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('list/<slug:data>', views.ListView, name='list'),
]