from django.conf.urls import url
from . import views
from . import ajax

urlpatterns = [


#General URLs
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^main/', views.main, name='main'),
    url(r'^joinlobby/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobby, name='joinlobby'),
    url(r'^deletelobby/(?P<id>\d+)/$', views.deletelobby, name='deletelobby'),

#Trivia URLs
    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),
    url(r'^trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),
    
    url(r'^triviasetup/(?P<id>\d+)/(?P<mode>\d+)/$', views.triviasetup, name='triviasetup'),
    url(r'^triviabegin/(?P<option>[-\w]+)/$', views.triviabegin, name='triviabegin'),
    url(r'^triviamode/', views.triviamode, name='triviamode'),
    url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^lobbytriviaoutcome/', views.lobbytriviaoutcome, name='lobbytriviaoutcome'),
    url(r'^triviaprocessing/(?P<option>[-\w]+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^trivianextquestion/', views.trivianextquestion, name='trivianextquestion'),
    url(r'^triviaend/', views.triviaend, name='triviaend'),


#Polla URLs
    url(r'^pollalobbies/', views.lobbypollaindex, name='lobbypollaindex'),
    url(r'^pollalobbiesdetails/(?P<id>\d+)/$', views.lobbypolladetails, name='lobbypolladetails'),
    url(r'^polla/', views.polla, name='polla'),
    url(r'^polladetails/(?P<id_p>\d+)/$', views.polla_apuesta, name='polladetails'),
    url(r'^pollaprocessing/(?P<option>[-\w]+)/(?P<id>\d+)/$', views.pollaprocessing, name='pollaprocessing'),
    url(r'^pollabet/', views.pollabet, name='pollabet'),
    url(r'^lobbypollaoutcome/', views.lobbypollaoutcome, name='lobbypollaoutcome'),
    url(r'^pollasetup/(?P<id>\d+)/$', views.pollasetup, name='pollasetup'),
    url(r'^deletelobbypolla/(?P<id>\d+)/$', views.deletelobbypolla, name='deletelobbypolla'),
    url(r'^joinlobbypolla/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobbypolla, name='joinlobbypolla'),

#Not Yet Assigned
    url(r'^equipolobbies/', views.lobbyequipoindex, name='lobbyequipoindex'),
    url(r'^equipolobbiesdetails/(?P<id>\d+)/$', views.lobbyequipodetails, name='lobbyequipodetails'),
    url(r'^equiposetup/(?P<id>\d+)/(?P<mode>\d+)/$', views.equiposetup, name='equiposetup'),
    url(r'^deletelobbyequipo/(?P<id>\d+)/$', views.deletelobbyequipo, name='deletelobbyequipo'),
    url(r'^joinlobbyequipo/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobbyequipo, name='joinlobbyequipo'),
    url(r'^ajax/get_players', ajax.get_players, name='ajax_get_players'),
    url(r'^teams/', views.TeamsView.as_view(), name='teams'),




];
