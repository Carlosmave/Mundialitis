from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import users, questions, answers, Partido, Polla
from .forms import RegisterForm, LoginForm, PollaForm
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
                    request.session.set_expiry(0)
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
        #return render(request, 'mundialitisapps/index.html')


def trivia(request):
    return render(request, 'mundialitisapps/indextrivia.html')




def index2(request):
    return render(request, 'mundialitisapps/app.html')

def index3(request):
    return render(request, 'mundialitisapps/conference.html')


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