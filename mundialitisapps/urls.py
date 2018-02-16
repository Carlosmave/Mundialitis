from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='main'),
    url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),



    url(r'^lobbytriviaindex/trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),



    #url(r'^trivia/details/', views.trivia, name='trivia'),
    #url(r'^$', views.Register, name='register'),
    #url(r'^$', views.index, name='index'),
    #url(r'^1/', views.index2, name='index2'),
    #url(r'^2/', views.index3, name='index3')

    url(r'^details/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.details, name='details'),
    url(r'^processing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.processing, name='processing'),

    #invitaciones
    url(r'^invitar/', views.invitar, name='invitar'),
    url(r'^perfil/', views.perfil, name='perfil'),
    
    url(r'^perfil1/', views.perfil1, name='perfil1'),
    url(r'^invitarusuario/', views.invitarusuario, name='invitarusuario'),
    url(r'^agregargrupo/', views.agregargrupo, name='agregargrupo'),
    url(r'^responderinvitacion/', views.responderinvitacion, name='responderinvitacion'),
    url(r'^useradmingroup/', views.useradmingroup, name='useradmingroup'),
    url(r'^misgrupos/', views.misgrupos, name='misgrupos'),
    url(r'^grupousuarios/', views.grupousuarios, name='grupousuarios'),
    url(r'^usuariosgrupo/', views.usuariosgrupo, name='usuariosgrupo')
];
