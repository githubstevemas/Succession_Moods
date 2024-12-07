from django.urls import path

from . import views

urlpatterns = [
    path('seasons', views.seasons, name='seasons'),
    path('graph/<str:character_name>/<str:season>/',
         views.character_seasons,
         name='character_seasons'),
]
