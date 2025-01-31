from django.urls import path
from . import views  # Importing the views from this app


urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
]