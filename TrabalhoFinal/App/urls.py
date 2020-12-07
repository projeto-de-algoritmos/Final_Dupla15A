from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.index, name='index'),
    path('search/path/', views.path_result, name='path_result'),
    path('search/error/', views.error, name='error'),
]