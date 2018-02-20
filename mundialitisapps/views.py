from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import users, questions, answers, lobbies,Invitacion
from .forms import RegisterForm, LoginForm, LobbyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserForm

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
                    #este es el original:

                    return HttpResponseRedirect('/main/')
                    #hacer esto para llamar datos de tabla users:


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
        userss = request.session.get('username')
        #context ={
        #'users' : userss
        #}
        #antes era 'mundialitisapps/main.html'
        #return render(request, '/perfil1/', context)
        return HttpResponseRedirect('/perfil1/')
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

# Mannejo de invitaciones:
#listo
def invitarusuario(request):
    info = request.POST
    invi=info.get('invitado','')
    grp=info.get('grupo','')
    username = request.session.get('username')
    invitadoexiste= users.objects.filter(username=invi).count()
    obj= 0
    obj = Invitacion.objects.filter(grupo=grp,invitado=invi).count()
    print ('asdaskdnojas')
    print (obj)
    if obj>=1:
        return HttpResponse("<script>alert('invitacion ya existe');document.location.href='/perfil';</script>")
    elif admingrupos(username,grp)==True and invitadoexiste==1:
        invit=Invitacion(invitado=invi,grupo=grp)
        invit.save()
        return HttpResponse("<script>alert('Se envio invitacion');document.location.href='/perfil';</script>")
    else:
        return HttpResponse("<script>alert('Usuario o grupo no existe');document.location.href='/perfil';</script>")

def agregargrupo(request):
    username = request.user.username
    info = request.POST
    gr=info.get('nombregrupo','')
    lista = grupo.objects.filter(nombre=gr).count()
    if lista ==1:
        #messages.info(request, 'Grupo ya existe')
        #return views.perfil(request)
        return HttpResponse("<script>alert('Grupo ya existe');document.location.href='/perfil';</script>")

    else:
        db_registro = grupo(nombre=gr,owner=username);
        db_registro.save()
        inv= Invitacion(invitado=username,owner=username,estado='aceptado',grupo=gr)
        inv.save()
        #return views.perfil(request)
        return HttpResponse("<script>alert('Grupo creado');document.location.href='/perfil';</script>")


def grupousuarios(grp):

    return None

""" Funcionaes de apoyo"""

#lista de usuarios de un grupo
def listausuarios(rgrupo):
    nombre='aceptado'
    lista = Invitacion.objects.filter(group=rgrupo,invitado=nombre)
    #gp = grupo.objects.filter(nombre=rgrup).count()
    usuarios=[]
    pass
    #return HttpResponse()

#si el nombre es administrador de grupo retorna true
#listo
def admingrupos(nombre,rgrupo):
    lista= lobbies.objects.filter(players=nombre,name=rgrupo).count()
    if lista==1:
        return (True)
    else:
        return False

#retorna invitaciones pendientes
#listo
def invitaciones(ruser):
    p=Invitacion.objects.filter(invitado=ruser,estado='pendiente')
    datos=[]
    for i in p:
        datos.append(i.grupo)
    return datos
#aceptar o rechazar invitacion
#listo
def responderinvitacion(request):
    info = request.POST
    rgrupo=info.get('grupo')
    ruser=request.session.get('username')
    rpta=info.get('rpta')
    obj = Invitacion.objects.get(grupo=rgrupo,invitado=ruser)
    obj.estado=rpta
    obj.save()
    if rpta=='aceptado':
        return HttpResponse("<script>alert('Grupo aceptado');document.location.href='/perfil1';</script>")
    else:
        return HttpResponse("<script>alert('Grupo rechazado');document.location.href='/perfil1';</script>")
#retorna los grupos donde el usaurio es admin
#listo
def useradmingroup(ruser):
    rpta=[]
    lista= lobbies.objects.filter(players=ruser)
    for i in lista:
        rpta.append(i.name)
    return rpta

#retorna una lista de los grupos a los que pertenece un usuario
def misgrupos(ruser):
    rpta=[]
    lista= Invitacion.objects.filter(invitado=ruser,estado='aceptado')
    for i in lista:
        if i.estado=='aceptado':

            rpta.append(i.grupo)
    return rpta
#retorna usuarios de un grupo
def usuariosgrupo(rgrupo):
    rpta=[]
    lista = Invitacion.objects.filter(grupo=rgrupo)
    for i in lista:
        if i.estado=='aceptado':
            rpta.append(i.invitado)
    return rpta

#otro mas, para que jale los datos al entrar al main
#listo
def perfil(request):

    usern = request.session.get('username')
    if request.method=='POST':

        print (request)
        context = { #'Invitaciones': invitaciones(usern),
        'users' : usern,
        'grupos': useradmingroup(usern),
        #'misgrupos': misgrupos(usern),
        #'listausuarios':views.usuariosgrupo(request.POST.get('sometext'),)
        }
        return render(request,'mundialitisapps/invitar.html',context)
    else:

        context = { #'Invitaciones': invitaciones(usern),
        'users' : usern,
        'grupos': useradmingroup(usern),
        #'misgrupos': misgrupos(usern)
        }
        return render(request,'mundialitisapps/invitar.html',context)

#probando
def perfil1(request):

    usern = request.session.get('username')
    p=Invitacion.objects.filter(invitado=usern,estado='pendiente').count

    if request.method=='POST':

        print (request)
        context = { 'Invitaciones': invitaciones(usern),
        'grupos': useradmingroup(usern),
        'users' : usern,
        'con' : p,
        #'misgrupos': misgrupos(usern),
        #'listausuarios':views.usuariosgrupo(request.POST.get('sometext'),)
        }
        return render(request,'mundialitisapps/main.html',context)
    else:

        context = { 'Invitaciones': invitaciones(usern),
        'grupos': useradmingroup(usern),
        'users' : usern,
        'con' : p,
        #'misgrupos': misgrupos(usern)
        }
        return render(request,'mundialitisapps/main.html',context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return HttpResponseRedirect('/loguot/')
