from django.urls import path
from rango import views  # Importing the views from this app

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('upload/', views.upload_image, name='upload'), # Image upload route
    path('gallery/', views.gallery, name='gallery'), # Image gallery route
]