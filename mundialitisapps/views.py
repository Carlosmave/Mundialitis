from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import User, Question, Answer, Lobby, Partido, Player
from .forms import RegisterForm, LoginForm, LobbyForm, CompleteRegForm, TeamForm
from django.contrib import messages
import random
# Create your views here.

#General Functions
def index(request):
    if (request.method == 'POST' and 'register' in request.POST):
        form=RegisterForm(request.POST)
        if form.is_valid():
            regusername=request.POST.get('regusername', '')
            regpassword=request.POST.get('regpassword', '')
            regpassword2=request.POST.get('regpassword2', '')
            if regpassword==regpassword2:
                exts = User.objects.filter(username=regusername).exists()
                if exts == False:
                    user_obj = User(username=regusername, password=regpassword, money=0)
                    user_obj.save()
                    return initialize(request, regusername, 'register')
                else:
                    messages.info(request, 'El usuario ya existe')
                    return render(request, 'mundialitisapps/index.html')
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
                    return initialize(request, logusername, 'login')
                else:
                    messages.info(request, 'Los datos no coinciden')
                    return render(request, 'mundialitisapps/index.html')
    else:
        form=RegisterForm()
        form2=LoginForm()
    return render(request, 'mundialitisapps/index.html', {'form':form, 'form2':form2,})


def initialize(request, username, mode):
    request.session['username'] = username
    if mode == 'register':
        return HttpResponseRedirect('/register/')
    elif mode == 'login':
        request.session['is_logged'] = 'true'
        request.session.set_expiry(0) #Esto significa que la sesion expira al cerrar el navegador
        return HttpResponseRedirect('/main/')


def register(request):
    if (request.method == 'POST' and 'cmpregister' in request.POST):
        form = CompleteRegForm(request.POST)
        if form.is_valid():
            User.objects.filter(username=request.session.get('username')).update(firstname = request.POST.get('regfirstname', ''), lastname = request.POST.get('reglastname', ''),
            email = request.POST.get('regemail', ''), address = request.POST.get('regaddress', ''), country = request.POST.get('regcountry', ''), money = request.POST.get('regmoney', ''))
            return initialize(request, request.session.get('username'), 'login')
    else:
        form=CompleteRegForm()
    return render(request, 'mundialitisapps/register.html', {'form':form})


def main(request):
    if request.session.get('is_logged') == 'true': ##esto se tendra que hacer a varias paginas para evitar el acceso por url sin login ##setear a false para cerrar sesion, de modo que no se pueda volver a entrar
        return render(request, 'mundialitisapps/main.html')
    else:
        return HttpResponseRedirect('/')

#Trivia Functions
def lobbytriviaindex(request):
    if (request.method == 'POST' and 'createlobby' in request.POST):
        form=LobbyForm(request.POST)
        form.fields['lobbypassword'].required = False
        if form.is_valid():
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            lobbymoney=request.POST.get('lobbymoney', '')
            exts=Lobby.objects.filter(name=lobbyname).exists()
            if exts == False:
                if lobbypassword == '':
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), ltype="Público", game="Trivia", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    lob = Lobby.objects.get(name=lobbyname)
                    return HttpResponseRedirect('/trivialobbiesdetails/' + str(lob.id))
                else:
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, ltype="Privado", game="Trivia", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    lob = Lobby.objects.get(name=lobbyname)
                    return HttpResponseRedirect('/trivialobbiesdetails/' + str(lob.id))
            else:
                messages.info(request, 'Ya hay un lobby con ese nombre')
                tlobbies=Lobby.objects.all().filter(game='Trivia')
                context = {'tlobbies':tlobbies}
                return render(request, 'mundialitisapps/lobbytriviaindex.html', context)
    else:
        form=LobbyForm()
        tlobbies=Lobby.objects.all().filter(game='Trivia')
        context = {'tlobbies':tlobbies}
        return render(request, 'mundialitisapps/lobbytriviaindex.html', context)
    return render(request, 'mundialitisapps/lobbytriviaindex.html', {'form':form})


def lobbytriviadetails(request, id):
    tlobby = Lobby.objects.get(id=id)
    if(tlobby.lstatus != "Terminado"):
        context = {'tlobby':tlobby}
        return render(request, 'mundialitisapps/lobbytriviadetailsnew.html', context)
    else:
        return HttpResponseRedirect('/trivialobbies/')



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





def trivia(request):
    actualid=request.session.get('question')
    actualttlscore=request.session.get('ttlscore')
    if actualid == None and actualttlscore == None: #borrarelttlscore  #podria omitir el if si arriba en vez de inicializarlo en none lo inicializo en 1 y 0
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
    actualid=request.session.get('question')
    mode=request.session.get('gamemode')

    if mode == "Fácil":
        if actualid < 10:  #if actualid < 10:
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

            if (((objlobby.players.count(","))+1) == (objlobby.playerscores.count(","))):
                lps=objlobby.playerscores.split(',')
                highestscore=-1
                winner=''
                for x in (0, (len(lps)-2)):
                    splayerscore = lps[x]
                    datascore = splayerscore.split(':')
                    score=(datascore[1])[:1]
                    if (int(datascore[1])>highestscore):
                        highestscore = int(datascore[1])
                        winner=datascore[0]


                objlobby.lstatus = "Terminado"
                objlobby.winner = winner
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

            if (((objlobby.players.count(","))+1) == (objlobby.playerscores.count(","))):
                lps=objlobby.playerscores.split(',')
                highestscore=-1
                winner=''
                for x in (0, (len(lps)-2)):
                    splayerscore = lps[x]
                    datascore = splayerscore.split(':')
                    score=(datascore[1])[:1]
                    if (int(datascore[1])>highestscore):
                        highestscore = int(datascore[1])
                        winner=datascore[0]


                objlobby.lstatus = "Terminado"
                objlobby.winner = winner
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

            if (((objlobby.players.count(","))+1) == (objlobby.playerscores.count(","))):
                lps=objlobby.playerscores.split(',')
                highestscore=-1
                winner=''
                for x in (0, (len(lps)-2)):
                    splayerscore = lps[x]
                    datascore = splayerscore.split(':')
                    score=(datascore[1])[:1]
                    if (int(datascore[1])>highestscore):
                        highestscore = int(datascore[1])
                        winner=datascore[0]


                objlobby.lstatus = "Terminado"
                objlobby.winner = winner
                objlobby.save()



            return HttpResponseRedirect('/lobbytriviaoutcome/')



def lobbytriviaoutcome(request):
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    context={'objlobby': objlobby}
    return render(request, 'mundialitisapps/lobbytriviaoutcome.html', context)


def triviaend(request):
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    winner=objlobby.winner
    money=objlobby.moneybet
    numplayers = objlobby.players.count(",")
    players = objlobby.players.split(",")
    for x in (0, numplayers):
        player = User.objects.get(username=players[x])
        actualmoney = player.money
        if players[x] == winner:
            player.money = actualmoney + numplayers*money
            player.save()
        else:
            player.money = actualmoney - money
            player.save()
    return deletelobby(request, lobbyid)





















#################INICIO FUNCIONES DE OTROS JUEGOS############################

def lobbypollaindex(request):
    if (request.method == 'POST' and 'createlobbypolla' in request.POST):
        form=LobbyForm(request.POST)
        form.fields['lobbypassword'].required = False
        if form.is_valid():  #si esto no se cumple se ira defrente a lo de fuera del if else, sin pasar por el else, ya que llego a entrar al if, pero dentro ya no continuo porque no habia un else mas. Esto estaria mal
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            lobbymoney=request.POST.get('lobbymoney', '')
            exts=Lobby.objects.filter(name=lobbyname).exists()
            if exts == False:
                if lobbypassword == '':
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), ltype="Público", game="Polla", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/pollalobbies/')
                    #Esto verlo despues a donde redirigira por ahora a la pagina principal de trivia
                else:
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, ltype="Privado", game="Polla", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/pollalobbies/')
            else:
                #messages.info(request, 'Ya hay un lobby con ese nombre') #para lo de mensajes use render, pero si uso render aca no se mostraran los lobbys existentes, ver si se puede hacer mensaje con returnredirect
                #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                #return HttpResponseRedirect(request, '/trivialobbies/')
                #request.session['lobbymessage'] = 'Ya hay un lobby con ese nombre'
                #return HttpResponseRedirect('/trivialobbies/')
                messages.info(request, 'Ya hay un lobby con ese nombre')
                tlobbies=Lobby.objects.all().filter(game='Polla')
                context = {
                    'tlobbies':tlobbies
                }
                return render(request, 'mundialitisapps/lobbypollaindex.html', context)
    else:
        form=LobbyForm()
        tlobbies=Lobby.objects.all().filter(game='Polla')
        context = {
            'tlobbies':tlobbies
        }
        return render(request, 'mundialitisapps/lobbypollaindex.html', context)
    return render(request, 'mundialitisapps/lobbypollaindex.html', {
    'form':form,
    })

def lobbyequipoindex(request):
    if (request.method == 'POST' and 'createlobbyequipo' in request.POST):
        form=LobbyForm(request.POST)
        form.fields['lobbypassword'].required = False
        if form.is_valid():  #si esto no se cumple se ira defrente a lo de fuera del if else, sin pasar por el else, ya que llego a entrar al if, pero dentro ya no continuo porque no habia un else mas. Esto estaria mal
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            lobbymoney=request.POST.get('lobbymoney', '')
            exts=Lobby.objects.filter(name=lobbyname).exists()
            if exts == False:
                if lobbypassword == '':
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), ltype="Público", game="Arma tu Equipo", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/equipolobbies/')
                    #Esto verlo despues a donde redirigira por ahora a la pagina principal de trivia
                else:
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, ltype="Privado", game="Arma tu Equipo", administrator=request.session.get('username'), moneybet=lobbymoney)
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/equipolobbies/')
            else:
                #messages.info(request, 'Ya hay un lobby con ese nombre') #para lo de mensajes use render, pero si uso render aca no se mostraran los lobbys existentes, ver si se puede hacer mensaje con returnredirect
                #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                #return HttpResponseRedirect(request, '/trivialobbies/')
                #request.session['lobbymessage'] = 'Ya hay un lobby con ese nombre'
                #return HttpResponseRedirect('/trivialobbies/')
                messages.info(request, 'Ya hay un lobby con ese nombre')
                tlobbies=Lobby.objects.all().filter(game='Arma tu Equipo')
                context = {
                    'tlobbies':tlobbies
                }
                return render(request, 'mundialitisapps/lobbyequipoindex.html', context)
    else:
        form=LobbyForm()
        tlobbies=Lobby.objects.all().filter(game='Arma tu Equipo')
        context = {
            'tlobbies':tlobbies
        }
        return render(request, 'mundialitisapps/lobbyequipoindex.html', context)
    return render(request, 'mundialitisapps/lobbyequipoindex.html', {
    'form':form,
    })

def lobbypolladetails(request, id):
    tlobby = Lobby.objects.get(id=id)
    if(tlobby.lstatus != "Terminado"):
        context = {
        'tlobby':tlobby,
        }
        return render(request, 'mundialitisapps/lobbypolladetailsnew.html', context)
    else:
        return HttpResponseRedirect('/pollalobbies/')

def lobbyequipodetails(request, id):
    tlobby = Lobby.objects.get(id=id)
    if(tlobby.lstatus != "Terminado"):
        context = {
        'tlobby':tlobby,
        }
        return render(request, 'mundialitisapps/lobbyequipodetailsnew.html', context)
    else:
        return HttpResponseRedirect('/equipolobbies/')

def deletelobbypolla(request, id):
    Lobby.objects.filter(id=id).delete()
    return HttpResponseRedirect('/pollalobbies/')

def joinlobbypolla(request, id, player):
    obj=Lobby.objects.get(id=id)
    actualplayers=obj.players
    if player in actualplayers:
        return HttpResponseRedirect('/pollalobbiesdetails/'+id)
    else:
        newplayers=actualplayers + ',' + player
        obj.players = newplayers
        obj.save()
        return HttpResponseRedirect('/pollalobbiesdetails/'+id)



def pollasetup(request, id):
    request.session['question'] = None
    request.session['ttlscore'] = 0
    request.session['processed'] = 'false'
    request.session['identifier'] = '' #poner esto más arriba
    request.session['idtlobbybegin'] = id
    objlob = Lobby.objects.get(id=request.session.get('idtlobbybegin'))
    objlob.lstatus = "Iniciado"
    objlob.save()
    return HttpResponseRedirect('/polla/')

def polla(request):
    user=User.objects.get(username=request.session.get('username'))
    partidos = Partido.objects.all()
    # configurar resultados
    #for partido in partidos:
    #    resultado = PollaPartido.objects.filter(id_partido = partido)[:1]
    #    if not resultado:
    #        # crea row partido para grabar resultados
    #        PollaPartido.objects.create(id_partido = partido)
    # init setup apuestas
    #for partido in partidos:
    #    polla_partido = PollaPartido.objects.get(id_partido=partido)
    #    ap = PollaApuesta.objects.filter(user=user, polla_partido=polla_partido)[:1]
    #    if not ap:
    #        # creates rows for displays
    #        PollaApuesta.objects.create(user=user, polla_partido=polla_partido)

    #apuestas = PollaApuesta.objects.filter(user=user).order_by('id')
    context = {
        'partidos' : partidos,
    }
    return render(request, 'mundialitisapps/pollaitselfindex.html', context)


def polla_apuesta(request, id_p):
    partido = Partido.objects.get(id=id_p)
    context={
    'partido':partido
    }

    return render(request, 'mundialitisapps/pollaitself.html', context)

def pollaprocessing(request, option, id):
    request.session['processed'] = 'true'
    partido = Partido.objects.get(id=id)
    request.session['identifier'] = request.session.get('identifier') + partido.identifier
    if (partido.resultado.replace(" ", "") == option):
        request.session['ttlscore'] = int(request.session.get('ttlscore')) + 1
    return HttpResponseRedirect('/polladetails/' +id)

def pollabet(request):
    request.session['processed'] = 'finished'
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    actualplayerscores=objlobby.playerscores
    objlobby.playerscores = actualplayerscores + request.session.get('username') + ": " + str(request.session.get('ttlscore')) + ","
    objlobby.save()
    if (((objlobby.players.count(","))+1) == (objlobby.playerscores.count(","))):
        lps=objlobby.playerscores.split(',')
        highestscore=-1
        winner=''
        for x in (0, (len(lps)-2)):
            splayerscore = lps[x]
            datascore = splayerscore.split(':')
            score=(datascore[1])[:1]
            if (int(datascore[1])>highestscore):
                highestscore = int(datascore[1])
                winner=datascore[0]


        objlobby.lstatus = "Terminado"
        objlobby.winner = winner
        objlobby.save()



    return HttpResponseRedirect('/lobbypollaoutcome/')

def lobbypollaoutcome(request):
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    context={'objlobby': objlobby}
    return render(request, 'mundialitisapps/lobbypollaoutcome.html', context)


def pollaend(request):
    lobbyid=request.session.get('idtlobbybegin')
    objlobby=Lobby.objects.get(id=lobbyid)
    winner=objlobby.winner
    money=objlobby.moneybet
    numplayers = objlobby.players.count(",")
    players = objlobby.players.split(",")
    for x in (0, numplayers):
        player = User.objects.get(username=players[x])
        actualmoney = player.money
        if players[x] == winner:
            player.money = actualmoney + numplayers*money
            player.save()
        else:
            player.money = actualmoney - money
            player.save()
    #player = User.objects.get(username=players[x])
    #actualmoney = player.money
    return deletelobby(request, lobbyid)








    #if (option==)

def polla_resultado(request):
    participantes = PollaApuesta.objects.all().distinct('user')
    polla_resultado = PollaPartido.objects.all()
    for participante in participantes:
        polla_puntos = PollaPuntaje.objects.filter(user=participante.user)[:1]
        if not polla_puntos:
            PollaPuntaje.objects.create(user=participante.user)
    polla_puntos = PollaPuntaje.objects.all()
    # calcular goles
    rng = random.random()
    for partido in polla_resultado:
        if rng < 0.33:
            e_ganador = partido.id_partido.equipo_a
        elif rng < 0.67:
            e_ganador = partido.id_partido.equipo_b
        else:
            e_ganador = 'Empate'
        partido.ganador = e_ganador
        partido.save()

    #listar personas con puntaje
    for participante in participantes:
        apuestas = PollaApuesta.objects.filter(user=participante.user)
        puntos = 0
        for apuesta in apuestas:
            p = PollaPartido.objects.get(id_partido=apuesta.polla_partido.id_partido)
            if apuesta.apuesta == p.ganador:
                puntos+=1
        puntaje = PollaPuntaje.objects.get(user_id=participante.user)
        puntaje.puntaje = puntos
        puntaje.save()

    participantes = PollaPuntaje.objects.all().order_by('-puntaje')
    context = {
        'participantes': participantes,
    }
    return render(request, 'mundialitisapps/polla_resultado.html', context)











def equiposetup(request, id, mode):
    request.session['question'] = None
    request.session['ttlscore'] = None
    request.session['processed'] = 'false'
    request.session['idtlobbybegin'] = id
    return HttpResponseRedirect('/equipo/')





def deletelobbyequipo(request, id):
    Lobby.objects.filter(id=id).delete()
    return HttpResponseRedirect('/equipolobbies/')

def joinlobbyequipo(request, id, player):
    obj=Lobby.objects.get(id=id)
    actualplayers=obj.players
    if player in actualplayers:
        return HttpResponseRedirect('/equipolobbiesdetails/'+id)
    else:
        newplayers=actualplayers + ',' + player
        obj.players = newplayers
        obj.save()
        return HttpResponseRedirect('/equipolobbiesdetails/'+id)
######FIN FUNCIONES DE OTROS JUEGOS##############
################FUNCIONES DE TRIVIA########################


##########
# Equipo #
##########

class TeamsView(TemplateView):
    template_name = 'mundialitisapps/teams.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TeamsView, self).get_context_data(*args, **kwargs)
        context['form'] = TeamForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = TeamForm(request.POST)
        resultado = 0
        if form.is_valid():
            ids = [v for k, v in form.cleaned_data.items() if k not in ['jugadores', 'selecciones', 'posiciones']]
            jugadores = Player.objects.filter(id__in=ids)
            for jugador in jugadores:
                resultado += jugador.puntaje
        context['resultado'] = resultado
        return self.render_to_response(context=context)
