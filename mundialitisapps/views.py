from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import User, Question, Answer, Lobby, Partido, Polla, PollaApuesta, PollaPartido, PollaPuntaje, Player
from .forms import RegisterForm, LoginForm, LobbyForm, CompleteRegForm, PollaForm, TeamForm

from django.contrib import messages
import random
# Create your views here.


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
                    request.session['username'] = regusername
                    return HttpResponseRedirect('/register/')
                    #return render(request, 'mundialitisapps/index.html')
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
    return render(request, 'mundialitisapps/index.html', {'form':form, 'form2':form2,})


def register(request):
    if (request.method == 'POST' and 'cmpregister' in request.POST):
        form4 = CompleteRegForm(request.POST)
        if form4.is_valid():
            regfirstname=request.POST.get('regfirstname', '')
            reglastname=request.POST.get('reglastname', '')
            regemail=request.POST.get('regemail', '')
            regaddress=request.POST.get('regaddress', '')
            regcountry=request.POST.get('regcountry', '')
            regmoney=request.POST.get('regmoney', '')
            user_obj = User.objects.get(username=request.session.get('username'))
            user_obj.address = regaddress
            user_obj.country = regcountry
            user_obj.email = regemail
            user_obj.firstname = regfirstname
            user_obj.lastname = reglastname
            user_obj.money = regmoney
            user_obj.save()
            request.session['is_logged'] = 'true'
            request.session.set_expiry(0)
            return HttpResponseRedirect('/main/')
    else:
        form4=CompleteRegForm()
    return render(request, 'mundialitisapps/register.html', {'form4':form4})


#def completeregistration(request):





















def main(request):
    is_logged=request.session.get('is_logged') ##esto se tendra que hacer a varias paginas para evitar el acceso por url sin login
    if is_logged == 'true': ##setear a false para cerrar sesion, de modo que no se pueda volver a entrar
        return render(request, 'mundialitisapps/main.html')
    else:
        return HttpResponseRedirect('/')

        #return render(request, 'mundialitisapps/index.html') Esto estaba mal por ejemplo porque dejaba el main ingresado manualmente arriba, lo que significaba
        #que en localhost:8000/main se renderizaba index.html lo que causaba problemas al loguearse o registrarse correctamente, con responseredirect te envia
        #a localhost:8000/ que es lo correcto
        #Explorar como utilizar el responseredirect para armar links mas complejos y luego utilizarlos con urls, y también
        #utilizar el render simultaneamente, response redirect arma links de 0 tener esto en cuenta (por ejemplo el return /main/ de arriba en la funcion indexx
        #podria ser un url mas complejo como /main/userlogged/ y en urls en vez de main/ poner main/userlogged/)(este ejemplo ultimo se puede utilizar con los
        #que defrente tengan responseredirect para hacer links mas complejos sin embargo si primero es un href y luego pasa a urls y luego a views, para utilizar
        #el responseredirect tendria que en el views poner el responseredirect para que te envie de nuevo a urls y de vuelta a views, por lo que seria trabajo
        #extra por las puras, por ello con los de href no conviene, solo conviene con los que tienen responseredirect defrente que son los que usan post,
        #igual hacer los links lo mas simple posible. Href y responseredirect construyen links y te mandan a urls, para luego ir a views; mientras que render
        #SOLO RENDERIZA LA PAGINA NADA MAS en el link indicado, donde esta indicado, no ejecuta funciones, por lo que si debo ejecutar funciones debo usar requestredirect)
        #RECORDAR QUE LAS FUNCIONES SE EJECUTAN DE ACUERDO/DEPENDIENDO AL URL EN EL QUE TE ENCUENTRES




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
                #messages.info(request, 'Ya hay un lobby con ese nombre') #para lo de mensajes use render, pero si uso render aca no se mostraran los lobbys existentes, ver si se puede hacer mensaje con returnredirect
                #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                #return HttpResponseRedirect(request, '/trivialobbies/')
                #request.session['lobbymessage'] = 'Ya hay un lobby con ese nombre'
                #return HttpResponseRedirect('/trivialobbies/')
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
    if(tlobby.lstatus != "Terminado"):
        context = {
        'tlobby':tlobby,
        }
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
        if actualid < 3:
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
    #player = User.objects.get(username=players[x])
    #actualmoney = player.money
    return deletelobby(request, lobbyid)
    #return HttpResponseRedirect('/trivialobbies/')
    #return render(request, 'mundialitisapps/lobbytriviaoutcome.html', context)



    #return render(request, 'mundialitisapps/lobbytriviaoutcome.html')

#§ solo aqui hacer las comparaciones de longitudes de listas, en el lobbytriviaoutcome solo revisar si el estado es terminado
    #len no funciona :v
    #poner todo esto dentro de trivia, ya no es necesaria esta funcion, pero para que no se ejecute siempre poner un condicional para que solo pase si ya termino
    #pensar si hacer esto o simplemente bloquear todos los botones de unir
    #si jugador sale bloquear botones, si creador sale si permitirle acceso para cerrarlo
    # ver si metod el lstatus=Iniciado dentro de la funcion trivia
    #decidir si al salir de la pagina el usuario puede volver a ver sus resultados o ya no, si tiene acceso a los botones o ya no

    #actualmente si ya cerro en trivialobbies, ni usuario ni administrador pueden entrar. Pero si retroceden en el navegador al usuario dejarlo entrar a ver sus resultados y a administradortambien (opcional)
    #es opcional porque se supone que si el usuario presiona continuar se irá a trivialobbies y ya no podrá acceder al lobby, solo le llegara o se le quitara el dinero
    #y el administrador no debe cerrar hasta que se le muestre el mensaje de ya termino y lo cierre mostrarlo como instruccion
    #preferentemente dejar el lobbytriviaoutcome independiente y no meterlo en el trivia

def polla(request):
    username = request.session.get('username')
    user=User.objects.get(username=username)
    partidos = Partido.objects.all()
    # configurar resultados
    for partido in partidos:
        resultado = PollaPartido.objects.filter(id_partido = partido)[:1]
        if not resultado:
            # crea row partido para grabar resultados
            PollaPartido.objects.create(id_partido = partido)

    # init setup apuestas
    for partido in partidos:
        polla_partido = PollaPartido.objects.get(id_partido=partido)
        ap = PollaApuesta.objects.filter(user=user, polla_partido=polla_partido)[:1]
        if not ap:
            # creates rows for displays
            PollaApuesta.objects.create(user=user, polla_partido=polla_partido)

    apuestas = PollaApuesta.objects.filter(user=user).order_by('id')

    # apuestas = PollaApuesta.objects.filter(id_user = user)

    # maybe move to results button?
    '''

    '''
    context = {
        'apuestas' : apuestas,
    }
    return render(request, 'mundialitisapps/pollaindex.html', context)

# configurar apuesta
def polla_apuesta(request, id_p):
    partido = Partido.objects.get(id=id_p)
    partidos = Partido.objects.all()
    username = request.session.get('username')
    user=User.objects.get(username=username)
    polla_partido = PollaPartido.objects.get(id_partido=partido)
    max_part = len(partidos)
    min_part = 1
    next_ele = int(id_p) + 1
    prev_ele = int(id_p) - 1
    apuesta_actual = PollaApuesta.objects.get(polla_partido=polla_partido,\
        user=user)
    # validation and goal assignation
    if request.method == 'POST':
        form = PollaForm(request.POST)
        if form.is_valid():
            ap = form.cleaned_data['apuesta']
            # definir apuesta
            apuesta = PollaApuesta.objects.get(polla_partido=polla_partido,\
                user=user)
            apuesta.apuesta = ap
            apuesta.save()
            messages.success(request, 'Ha apostado satisfactoriamente.')
            apuesta_actual = PollaApuesta.objects.get(polla_partido=polla_partido,\
                user=user)
            context = {
                'id_p' : id_p,
                'partido' : partido,
                'apuesta_actual' : apuesta_actual,
                'form': form,
                'prev_ele': prev_ele,
                'next_ele': next_ele,
                'max_part': max_part,
                'min_part': min_part,
            }
            return render(request, 'mundialitisapps/polla.html', context)
    else:
        form = PollaForm()

    context = {
        'id_p': id_p,
        'partido' : partido,
        'apuesta_actual' : apuesta_actual,
        'form' : form,
        'prev_ele': prev_ele,
        'next_ele': next_ele,
        'max_part': max_part,
        'min_part': min_part,
    }

    return render(request, 'mundialitisapps/polla.html', context)

def polla_resultado(request):
    participantes = PollaApuesta.objects.all().distinct('user')

    polla_resultado = PollaPartido.objects.all()
    polla_puntos = PollaPuntaje.objects.all()
    if not polla_puntos:
        for participante in participantes:
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





def begin(request):
    return render(request, 'mundialitisapps/triviaitself.html')
