from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Question, Answer, Lobby, Partido, Polla, PollaApuesta, PollaPartido
from django.forms import formset_factory
from .forms import RegisterForm, LoginForm, PollaForm, LobbyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import random

def index(request):
    if (request.method == 'POST' and 'register' in request.POST):
        form=RegisterForm(request.POST) ##AQUI TAMBIEN LO DE PROBAR LA TABLA
        if form.is_valid():

            regusername=request.POST.get('regusername', '')
            regpassword=request.POST.get('regpassword', '')
            regpassword2=request.POST.get('regpassword2', '')

            if regpassword==regpassword2:
                exts = User.objects.filter(username=regusername).exists()
                if exts == False:
                    user_obj = User(username=regusername, password=regpassword)  ##AQUI PROBAR USAR LA TABLA DEFAULT DE DJANGO
                    user_obj.save()
                    #return HttpResponseRedirect(reverse('jobs:cost'))
                    return render(request, 'mundialitisapps/index.html')
                else:
                    messages.info(request, 'El usuario ya existe')
                    return render(request, 'mundialitisapps/index.html')
                    #return render_to_response('mundialitisapps/index.html', {"message": El usuario ya existe});
            else:
                messages.info(request, 'Las contraseñas no coinciden')
                return render(request, 'mundialitisapps/index.html')

    elif (request.method == 'POST' and 'login' in request.POST):
        form2=LoginForm(request.POST)
        if form2.is_valid():
            logusername=request.POST.get('logusername', '')
            logpassword=request.POST.get('logpassword', '')
            exts = User.objects.filter(username=logusername).exists()
            if exts == False:
                messages.info(request, 'El usuario no existe')
                return render(request, 'mundialitisapps/index.html')
            else:
                usr=User.objects.get(username=logusername)
                usrp=usr.password
                if(usrp==logpassword):
                    request.session['username'] = logusername
                    request.session['userid'] = usr.id
                    request.session['is_logged'] = 'true'
                    request.session.set_expiry(0)  #esto significa que la sesion expira al cerrar el navegador
                    return HttpResponseRedirect('/main/')
                else:
                    messages.info(request, 'Los datos no coinciden')
                    return render(request, 'mundialitisapps/index.html')
    else:
        form=RegisterForm()
        form2=LoginForm()
    #return render(request, 'mundialitisapps/index.html', {
    return render(request, 'mundialitisapps/index.html', {
    'form':form, 'form2':form2,
    })

def main(request):
    is_logged=request.session.get('is_logged') ##esto se tendra que hacer a varias paginas para evitar el acceso por url sin login
    if is_logged == 'true': ##setear a false para cerrar sesion, de modo que no se pueda volver a entrar
        return render(request, 'mundialitisapps/main.html')
    else:
        return HttpResponseRedirect('/')

def lobbytriviaindex(request):
    if (request.method == 'POST' and 'createlobby' in request.POST):
        form3=LobbyForm(request.POST)
        form3.fields['lobbypassword'].required = False
        if form3.is_valid():  #si esto no se cumple se ira defrente a lo de fuera del if else, sin pasar por el else, ya que llego a entrar al if, pero dentro ya no continuo porque no habia un else mas. Esto estaria mal
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            lobbymoney=request.POST.get('lobbymoney', '')
            exts2=Lobby.objects.filter(name=lobbyname).exists()
            if exts2 == False:
                if lobbypassword == '':
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), ltype="Público", game="Trivia", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/trivialobbies/')
                    #Esto verlo despues a donde redirigira por ahora a la pagina principal de trivia
                else:
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, ltype="Privado", game="Trivia", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/trivialobbies/')
            else:
                messages.info(request, 'Ya hay un lobby con ese nombre')
                tlobbies=Lobby.objects.all().filter(game='Trivia')
                context = {
                    'tlobbies':tlobbies
                }
                return render(request, 'mundialitisapps/lobbytriviaindex.html', context)
    else:
        form3=LobbyForm()
        tlobbies=Lobby.objects.all().filter(game='Trivia')
        context = {
            'tlobbies':tlobbies
        }
        return render(request, 'mundialitisapps/lobbytriviaindex.html', context)
    return render(request, 'mundialitisapps/lobbytriviaindex.html', {
        'form3':form3,
    })

def lobbytriviadetails(request, id):
    tlobby = Lobby.objects.get(id=id)
    context = {
    'tlobby':tlobby,
    }
    return render(request, 'mundialitisapps/lobbytriviadetailsnew.html', context)


def deletelobby(request, id):
    Lobby.objects.filter(id=id).delete()
    return HttpResponseRedirect('/trivialobbies/')

def joinlobby(request, id, player):
    obj=Lobby.objects.get(id=id)
    actualplayers=obj.players
    if player in actualplayers:
        return HttpResponseRedirect('/trivialobbiesdetails/'+id)
    else:
        newplayers=actualplayers + ',' + player
        obj.players = newplayers
        obj.save()
        return HttpResponseRedirect('/trivialobbiesdetails/'+id)

def polla(request, id_p):
    # un solo partido
    partidos = Partido.objects.all()
    num_partidos = len(partidos)
    id_p = int(id_p)
    next_id = id_p+1
    estado = False
    if request.method == 'POST':
        if id_p < num_partidos:
            partido = Partido.objects.get(id=id_p)
            polla = Polla.objects.create()
            form = PollaForm()
            rng = random.random()
            if rng < 0.33:
                resultado = partido.equipo_a
            elif rng < 0.67:
                resultado = partido.equipo_b
            else:
                resultado = 'Empate'
            # graba el resultado al partido perteneciente a la polla
            polla_resultado = PollaPartido.objects.create(id_partido=partido,\
                ganador=resultado)
        if form.is_valid():           
            estado = True
            ap = form.cleaned_data['apuesta']
            # definir apuesta
            apuesta = PollaApuesta.create(id_polla_partido=polla_resultado,\
                id_user=request.user.id, apuesta=ap)
            
            context = {
                'id_p' : next_id,
                'partido' : partido,
                'form': form,
            }
            return render(request, 'mundialitisapps/polla.html', context)
    else:
        partido = Partido.objects.get(id=id_p)
        form = PollaForm()

    context = {
        'id_p' : next_id,
        'partido' : partido,
        'form' : form,
    }

    return render(request, 'mundialitisapps/polla.html', context)

def polla_resultado(request):
    participantes = PollaApuesta.objects.all().order_by('-puntos')
    

    context = {
        'participantes': participantes,
    }
    return render(request, 'mundialitisapps/polla_resultado.html', context)

def triviasetup(request, id, mode):
    request.session['question'] = None
    request.session['ttlscore'] = None
    request.session['processed'] = 'false'
    request.session['idtlobbybegin'] = id
    if mode == "1":
        return HttpResponseRedirect('/triviamode/')
    elif mode =="2":
        return HttpResponseRedirect('/trivia/')


def triviamode(request):
    return render(request, 'mundialitisapps/trivia.html')

def triviabegin(request, option):
    objlob = Lobby.objects.get(id=request.session.get('idtlobbybegin'))
    objlob.lstatus = "Iniciado"
    objlob.gamemode = option
    objlob.save()
    return HttpResponseRedirect('/trivia/')
    #return HttpResponseRedirect('/triviastart/')

def trivia(request):
    actualid=request.session.get('question')
    actualttlscore=request.session.get('ttlscore')
    if actualid == None and actualttlscore == None: #borrarelttlscore  #podria omitir el if si arriba en vez de inicializarlo en none lo inicializo en 1 y 0
        #id=1
        #ttlscore=0
        objlob = Lobby.objects.get(id=request.session.get('idtlobbybegin'))
        request.session['gamemode'] = objlob.gamemode
        request.session['question'] = 1
        request.session['ttlscore'] = 0
        return HttpResponseRedirect('/trivia/')
    else:
        triv = Question.objects.get(id=actualid)
        context={
        'triv':triv,
        }
        return render(request, 'mundialitisapps/triviaitself.html', context)

def triviaprocessing(request, option):
        #request.session['norld'] = "activated"
        request.session['processed'] = 'true'
        playeranswer=option
        objanswer = Answer.objects.get(id=request.session.get('question'))
        preanswer = objanswer.answer.replace(" ", "")
        correctanswer = preanswer.replace(",", "")
        questionscore = objanswer.score


        if correctanswer == playeranswer:
            request.session['triviamessage'] = 'Respuesta Correcta'
            request.session['questionscore'] = questionscore
            request.session['ttlscore'] = int(request.session.get('ttlscore'))+int(questionscore)

        else:
            request.session['triviamessage'] = 'Respuesta Incorrecta'
            request.session['questionscore'] = 0


        request.session['playeranswer'] = option
        return HttpResponseRedirect('/trivia/')



def trivianextquestion(request):
    #request.session['norld'] = "dectivated"
    actualid=request.session.get('question')

    mode=request.session.get('gamemode')

    if mode == "Fácil":
        if actualid < 10:
            request.session['processed'] = 'false'
            newid=int(actualid)+1
            request.session['question'] = newid
            return HttpResponseRedirect('/trivia/')
        else:
            request.session['processed'] = 'finished'
            lobbyid=request.session.get('idtlobbybegin')
            objlobby=Lobby.objects.get(id=lobbyid)
            actualplayerscores=objlobby.playerscores
            objlobby.playerscores = actualplayerscores + request.session.get('username') + ": " + str(request.session.get('ttlscore')) + ","
            objlobby.save()

            return HttpResponseRedirect('/lobbytriviaoutcome/')
    elif mode == "Intermedio":
        if actualid < 20:
            request.session['processed'] = 'false'
            newid=int(actualid)+1
            request.session['question'] = newid
            return HttpResponseRedirect('/trivia/')
        else:
            request.session['processed'] = 'finished'
            lobbyid=request.session.get('idtlobbybegin')
            objlobby=Lobby.objects.get(id=lobbyid)
            actualplayerscores=objlobby.playerscores
            objlobby.playerscores = actualplayerscores + request.session.get('username') + ": " + str(request.session.get('ttlscore')) + ","
            objlobby.save()

            return HttpResponseRedirect('/lobbytriviaoutcome/')
    elif mode == "Difícil":
        if actualid < 30:
            request.session['processed'] = 'false'
            newid=int(actualid)+1
            request.session['question'] = newid
            return HttpResponseRedirect('/trivia/')
        else:
            request.session['processed'] = 'finished'
            lobbyid=request.session.get('idtlobbybegin')
            objlobby=Lobby.objects.get(id=lobbyid)
            actualplayerscores=objlobby.playerscores
            objlobby.playerscores = actualplayerscores + request.session.get('username') + ": " + str(request.session.get('ttlscore')) + ","
            objlobby.save()

            return HttpResponseRedirect('/lobbytriviaoutcome/')

def lobbytriviaoutcome(request):
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    context={
    'objlobby': objlobby
    }
    return render(request, 'mundialitisapps/lobbytriviaoutcome.html', context)

def begin(request):
    return render(request, 'mundialitisapps/triviaitself.html')
