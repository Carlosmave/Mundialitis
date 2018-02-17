from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Question, Answer, Lobby
from .forms import RegisterForm, LoginForm, LobbyForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


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


def lobbytriviaindex(request):
    if (request.method == 'POST' and 'createlobby' in request.POST):
        form3=LobbyForm(request.POST)
        form3.fields['lobbypassword'].required = False
        if form3.is_valid():  #si esto no se cumple se ira defrente a lo de fuera del if else, sin pasar por el else, ya que llego a entrar al if, pero dentro ya no continuo porque no habia un else mas. Esto estaria mal
            lobbyname=request.POST.get('lobbyname', '')
            lobbypassword=request.POST.get('lobbypassword', '')
            exts2=Lobby.objects.filter(name=lobbyname).exists()
            if exts2 == False:
                if lobbypassword == '':
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), status="Público", game="Trivia", administrator=request.session.get('username'))
                    lobby_obj.save()
                    #return render(request, 'mundialitisapps/lobbytriviaindex.html')
                    return HttpResponseRedirect('/trivialobbies/')
                    #Esto verlo despues a donde redirigira por ahora a la pagina principal de trivia
                else:
                    lobby_obj = Lobby(name=lobbyname, players=request.session.get('username'), lobpass=lobbypassword, status="Privado", game="Trivia", administrator=request.session.get('username'))
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
        return HttpResponseRedirect('/trivialobbiesdetails/public/'+id)
    else:
        newplayers=actualplayers + ',' + player
        obj.players = newplayers
        obj.save()
        return HttpResponseRedirect('/trivialobbiesdetails/public/'+id)


def details(request, id, ttlscore):
    if int(id)<31:
        triv = Question.objects.get(id=id)
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
    triv = Question.objects.get(id=id)
    playeranswer=option
    objanswer = Answer.objects.get(id=id)
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
