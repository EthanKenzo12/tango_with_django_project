from django.urls import path
from . import views  # Importing the views from this app


urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
    path('upload/', views.upload_image, name='upload'), # Image upload route
    path('gallery/', views.gallery, name='gallery'), # Image gallery route
]