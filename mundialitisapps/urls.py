from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^main/', views.main, name='main'),

    url(r'^trivialobbies/', views.lobbytriviaindex, name='lobbytriviaindex'),


    url(r'^begin/', views.begin, name='begin'),


    url(r'^triviasetup/(?P<id>\d+)/(?P<mode>\d+)/$', views.triviasetup, name='triviasetup'),
    url(r'^triviabegin/(?P<option>[-\w]+)/$', views.triviabegin, name='triviabegin'),
    url(r'^triviamode/', views.triviamode, name='triviamode'),


    url(r'^trivia/', views.trivia, name='trivia'),
    url(r'^lobbytriviaoutcome/', views.lobbytriviaoutcome, name='lobbytriviaoutcome'),

    url(r'^triviaprocessing/(?P<option>[-\w]+)/$', views.triviaprocessing, name='triviaprocessing'),
    url(r'^trivianextquestion/', views.trivianextquestion, name='trivianextquestion'),

    url(r'^triviaend/', views.triviaend, name='triviaend'),



    url(r'^trivialobbiesdetails/(?P<id>\d+)/$', views.lobbytriviadetails, name='lobbytriviadetails'),
    url(r'^deletelobby/(?P<id>\d+)/$', views.deletelobby, name='deletelobby'),
    url(r'^joinlobby/(?P<id>\d+)/(?P<player>[-\w]+)/$', views.joinlobby, name='joinlobby'),

    url(r'^polla/$', views.polla, name='pollahome'),
    url(r'^polla/(?P<id_p>\d+)/$', views.polla_apuesta, name='polla'),
    url(r'^polla/resultados', views.polla_resultado, name='polla_resultado'),

];
