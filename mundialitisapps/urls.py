from django.conf.urls import url
from . import ajax
from . import views

urlpatterns = [
    url(r'^ajax/get_players', ajax.get_players, name='ajax_get_players'),
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='main'),
    url(r'^teams/', views.TeamsView.as_view(), name='teams'),
    url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),



    url(r'^lobbytriviaindex/trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),



    #url(r'^trivia/details/', views.trivia, name='trivia'),
    #url(r'^$', views.Register, name='register'),
    #url(r'^$', views.index, name='index'),
    #url(r'^1/', views.index2, name='index2'),
    #url(r'^2/', views.index3, name='index3')

    url(r'^details/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.details, name='details'),
    url(r'^processing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.processing, name='processing')
];
