from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('moods/', include('moods.urls')),
    path('seasons/', include('seasons.urls')),
    path('quotes/', include('quotes.urls')),
]
