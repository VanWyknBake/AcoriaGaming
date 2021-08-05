from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tour/', views.tourn, name='tournaments'),
    path('tour/codm/', views.codtourn, name='codm'),
    path('tour/f1/', views.f1tourn, name='f1'),
    path('tour/minecraft/', views.minecrafttourn, name='minecraft'),
    path('tour/arma/', views.armatourn, name='arma'),
    path('tour/cs/', views.cstourn, name='cs'),
    path('tour/ac/', views.actourn, name='ac'),
    path('streamers/', views.streamers, name='streamers'),

    
]
