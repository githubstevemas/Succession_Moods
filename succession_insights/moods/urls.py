from django.urls import path

from . import views

urlpatterns = [
    path('moods', views.moods, name='moods'),
    path('graph/<str:character_name>/', views.character_moods, name='character_moods')
]
