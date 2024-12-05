from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('seasons', views.seasons, name='seasons'),
    path('character_seasons/<str:character_name>/<int:season>/',
         views.character_seasons,
         name='character_seasons'),
    path('about', views.about, name='about'),
    path('moods/', include('moods.urls'))
]
