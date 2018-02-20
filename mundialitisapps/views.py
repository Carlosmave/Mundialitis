from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Questions, Answers, Lobbies, Partido, Polla, PollaApuesta, PollaPartido
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
        context = {
            'triv': triv,
            'message':'Respuesta Correcta',
            'qscore':questionscore,
            'ttlscore': int(ttlscore)+int(questionscore),
            'id':newid
        }
        return render(request, 'mundialitisapps/outcome.html', context)
    else:
        context2 = {
            'triv': triv,
            'message':'Respuesta Incorrecta',
            'qscore':0,
            'ttlscore': ttlscore,
            'id':newid
        }
        return render(request, 'mundialitisapps/outcome.html', context2)

def polla(request):
    if request.method == 'POST':
        partidos = Partido.objects.all()
        num_partidos = len(partidos)
        polla = Polla.objects.create()
        PollaFormset = formset_factory(PollaForm)
        form = PollaFormset()
        for partido in partidos:
            rng = random.random()
            if rng < 0.33:
                resultado = partido.equipo_a
            elif rng < 0.67:
                resultado = partido.equipo_b
            else:
                resultado = 'Empate'
            # graba el resultado al partido perteneciente a la polla
            polla_resultado = PollaPartido.objects.create(id_polla=polla.id,\
                id_partido=partido.id, ganador=resultado)
        if form.is_valid():            
            ap = form.cleaned_data['apuesta']
            # definir apuesta
            for partido in partidos:
                apuesta = PollaApuesta.create(id_pollaresultado=polla_resultado.id,\
                    id_user=request.user.id, apuesta=ap)
    else:
        partidos = Partido.objects.all()
        form = PollaForm()

    context = {
        'partidos' : partidos,
        'form' : form,
    }

    return render(request, 'mundialitisapps/polla.html', context)

def polla_resultado(request):
    usuarios = PollaApuesta.objects.all()

    context = {
        'ganadores' : ganadores,
    }
    return render(request, 'mundialitisapps/polla_resultado.html', context)