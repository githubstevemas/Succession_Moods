from django.urls import path

from . import views

urlpatterns = [
    path('quotes', views.quotes, name='quotes'),
]