from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('seasons', views.seasons, name='seasons'),
    path('graph/<str:character_name>/<str:season>/',
         views.character_seasons,
         name='character_seasons'),
    path('quotes', views.quotes, name='quotes'),
    path('about', views.about, name='about'),
    path('moods/', include('moods.urls'))
]
