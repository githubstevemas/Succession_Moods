from django.urls import path

from . import views

urlpatterns = [
    path('moods', views.moods, name='moods')
]
