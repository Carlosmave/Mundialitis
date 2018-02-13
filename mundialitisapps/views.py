from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
<<<<<<< HEAD
from .models import users, questions, answers, Partido, Polla
from .forms import RegisterForm, LoginForm, PollaForm
=======
from .models import users, questions, answers, lobbies
from .forms import RegisterForm, LoginForm, LobbyForm
>>>>>>> 06d0afcc691588639511583cd98163374526b61c
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

import random
#from .models import questions, answers
# Create your views here.
#def index(request):
#    return render(request, 'mundialitisapps/index.html')


def index(request):
    if (request.method == 'POST' and 'register' in request.POST):
        form=RegisterForm(request.POST) ##AQUI TAMBIEN LO DE PROBAR LA TABLA
        if form.is_valid():

            regusername=request.POST.get('regusername', '')
            regpassword=request.POST.get('regpassword', '')
            regpassword2=request.POST.get('regpassword2', '')

            if regpassword==regpassword2:
                exts = users.objects.filter(username=regusername).exists()
                if exts == False:
                    user_obj = users(username=regusername, password=regpassword)  ##AQUI PROBAR USAR LA TABLA DEFAULT DE DJANGO
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
            exts = users.objects.filter(username=logusername).exists()
            if exts == False:
                messages.info(request, 'El usuario no existe')
                return render(request, 'mundialitisapps/index.html')
            else:
                usr=users.objects.get(username=logusername)
                usrp=usr.password
                if(usrp==logpassword):
                    #return render(request, 'mundialitisapps/main.html')
                    #return HttpResponseRedirect('mundialitisapps/main/')
                    #check later if additional commas are needed
                    request.session['username'] = logusername
                    request.session['userid'] = usr.id
                    request.session['is_logged'] = 'true'
                    request.session.set_expiry(0)  #esto significa que la sesion expira al cerrar el navegador
                    return HttpResponseRedirect('/main/')
                else:
                    messages.info(request, 'Los datos no coinciden')
                    return render(request, 'mundialitisapps/index.html')

                #lllllllllllllllllllllllllllllll

    else:
        form=RegisterForm()
        form2=LoginForm()
    #return render(request, 'mundialitisapps/index.html', {
    return render(request, 'mundialitisapps/index.html', {
    'form':form, 'form2':form2,
    })


def main(request):
    is_logged=request.session.get('is_logged') ##esto se tendra que hacer a varias paginas
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



def trivia(request):
    return render(request, 'mundialitisapps/indextrivia.html')




def index2(request):
    return render(request, 'mundialitisapps/app.html')

def index3(request):
    return render(request, 'mundialitisapps/conference.html')















def lobbytriviaindex(request):
    if (request.method == 'POST' and 'createlobby' in request.POST):
        form3=LobbyForm(request.POST)
        form3.fields['lobbypassword'].required = False
        if form3.is_valid():  #si esto no se cumple se ira defrente a lo de fuera del if else, sin pasar por el else, ya que llego a entrar al if, pero dentro ya no continuo porque no habia un else mas. Esto estaria mal
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            exts2=lobbies.objects.filter(name=lobbyname).exists()
            if exts2 == False:
                if lobbypassword == '':
                    lobby_obj = lobbies(name=lobbyname, players=request.session.get('username'), status="Público", game="Trivia")
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/trivialobbies/')
                    #Esto verlo despues a donde redirigira por ahora a la pagina principal de trivia
                else:
                    lobby_obj = lobbies(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, status="Privado", game="Trivia")
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/trivialobbies/')
            else:
                messages.info(request, 'Ya hay un lobby con ese nombre') #para lo de mensajes use render, pero si uso render aca no se mostraran los lobbys existentes, ver si se puede hacer mensaje con returnredirect
                return render(request, 'mundialitisapps/lobbytriviaindex.html')
    else:
        form3=LobbyForm()
        tlobbies=lobbies.objects.all().filter(game='Trivia')
        context = {
            'title':'Trivia Lobbies',
            'tlobbies':tlobbies
        }
        return render(request, 'mundialitisapps/lobbytriviaindex.html', context)
    return render(request, 'mundialitisapps/lobbytriviaindex.html', {
    'form3':form3,
    })



#mi logica devolverla
#    tlobbies=lobbies.objects.all().filter(game='Trivia')
#    context = {
#        'title':'Trivia Lobbies',
#        'tlobbies':tlobbies
#    }
#    return render(request, 'mundialitisapps/lobbytriviaindex.html', context)





















def lobbytriviadetails(request, id):
    tlobbies = lobbies.objects.get(id=id)
    context = {
    'tlobbies':tlobbies
    }
    return render(request, 'mundialitisapps/lobbytriviadetails.html', context)



def details(request, id, ttlscore):
    if int(id)<31:
        triv = questions.objects.get(id=id)
        newid=int(id)+1
        context={
        'triv':triv,
        'id': newid,
        'ttlscore':ttlscore
        }
        return render(request, 'mundialitisapps/details.html', context)
    else:
        context={
        'ttlscore':ttlscore
        }
        return render(request, 'mundialitisapps/scorescreen.html', context)


def processing(request, option, id, ttlscore):
    newid=int(id)+1
    triv = questions.objects.get(id=id)
    playeranswer=option
    objanswer = answers.objects.get(id=id)
    preanswer = objanswer.answer.replace(" ", "")
    correctanswer = preanswer.replace(",", "")
    questionscore = objanswer.score

    if correctanswer == playeranswer:
        context={
        'triv': triv,
        'message':'Respuesta Correcta',
        'qscore':questionscore,
        'ttlscore': int(ttlscore)+int(questionscore),
        'id':newid
        }
        return render(request, 'mundialitisapps/outcome.html', context)
    else:
        context2={
        'triv': triv,
        'message':'Respuesta Incorrecta',
        'qscore':0,
        'ttlscore': ttlscore,
        'id':newid
        }
        return render(request, 'mundialitisapps/outcome.html', context2)

def pollaindex(request):
    #get id_usuario
    usuario = request.userid
    #get pollas asociadas a usuario
    pollas = PollaApuesta.objects.filter(id_usuario=usuario)

    return render(request, 'mundialitisapps/pollaindex.html')


def polla(request):
    # seleccionar partido
    partidos = Partido.objects.all()
    pk_partido = random.randint(1, len(partidos) - 1)
    partido = Partido.objects.get(pk=pk_partido)
    # crear row polla con partido seleccionado
    
    
    # calcular goles
    for i in range(2):
        rng = random.random()
        if rng < 0.33:
            resultado = partido.equipo_a
        elif rng < 0.67:
            resultado = partido.equipo_b
        else:
            resultado = 'Empate'
    polla = Polla.objects.create(id_partido=partido, ganador=resultado)
    
    # determinar apuesta
    if request.method == 'POST':
        form = PollaForm(request.POST)
        if form.is_valid():
            ap = form.cleaned_data['apuesta']
            # print(ap)
            if ap == polla.ganador:
                return HttpResponse("GANASTE")
            else:
                return HttpResponse("PERDISTE")
    else:
        form = PollaForm()

    context = {
        'form': form,
        'partido': partido,
    }

    return render(request, 'mundialitisapps/polla.html', context)