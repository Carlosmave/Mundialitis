from django.conf.urls import url
from . import ajax
from . import views

urlpatterns = [
    url(r'^ajax/get_players', ajax.get_players, name='ajax_get_players'),
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='main'),
    url(r'^teams/', views.TeamsView.as_view(), name='teams'),
    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),


    url(r'^begin/', views.begin, name='begin'),

    #url(r'^trivia/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.trivia, name='trivia'),
    url(r'^triviastart/', views.triviastart, name='triviastart'),
    #url(r'^triviagamemode/', views.triviagamemode, name='triviagamemode'),
    url(r'^trivia/', views.trivia, name='trivia'),
    #url(r'^triviaprocessing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^triviaprocessing/(?P<option>[-\w]+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^trivianextquestion/', views.trivianextquestion, name='trivianextquestion'),

    #url(r'^pruebita/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.pruebita, name='pruebita'),



    url(r'^trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),
    url(r'^deletelobby/(?P<id>\d+)/$', views.deletelobby, name='deletelobby'),
    url(r'^joinlobby/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobby, name='joinlobby'),
    #url(r'^details/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.details, name='details'),
    url(r'^processing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.processing, name='processing')
];
