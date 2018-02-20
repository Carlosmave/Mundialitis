from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='main'),
    #url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),


    url(r'^begin/', views.begin, name='begin'),

    #url(r'^trivia/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.trivia, name='trivia'),
    url(r'^triviasetup/(?P<id>\d+)/(?P<mode>\d+)/$', views.triviasetup, name='triviasetup'),
    url(r'^triviabegin/(?P<option>[-\w]+)/$', views.triviabegin, name='triviabegin'),
    url(r'^triviamode/', views.triviamode, name='triviamode'),
    #url(r'^triviastart/', views.triviastart, name='triviastart'),
    #url(r'^triviagamemode/', views.triviagamemode, name='triviagamemode'),
    url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^lobbytriviaoutcome/', views.lobbytriviaoutcome, name='lobbytriviaoutcome'),
    #url(r'^triviaprocessing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^triviaprocessing/(?P<option>[-\w]+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^trivianextquestion/', views.trivianextquestion, name='trivianextquestion'),

    #url(r'^pruebita/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.pruebita, name='pruebita'),



    url(r'^trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),
    url(r'^deletelobby/(?P<id>\d+)/$', views.deletelobby, name='deletelobby'),
    url(r'^joinlobby/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobby, name='joinlobby'),
    #url(r'^details/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.details, name='details'),
    #url(r'^processing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.processing, name='processing')
];
