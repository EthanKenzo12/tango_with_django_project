from django.urls import path
from rango import views  # Importing the views from this app

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('upload/', views.upload_image, name='upload'), # Image upload route
    path('gallery/', views.gallery, name='gallery'), # Image gallery route
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
]