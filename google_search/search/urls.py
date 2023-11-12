from django.urls import path
from . import views


app_name = "search"
urlpatterns = [
    path('', views.index, name='index'),
    path('images_search/', views.images_search, name='images_search'),
    path('advanced_search/', views.advanced_search, name='advanced_search'),
]