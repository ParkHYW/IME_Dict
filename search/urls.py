from django.urls import path
from . import views


app_name = 'search'

urlpattern = [
    path('', views.searchResult, name='searchResult'),
]