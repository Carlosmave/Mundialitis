from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import users
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from .models import questions, answers
# Create your views here.
#def index(request):
#    return render(request, 'mundialitisapps/index.html')

def index(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():

            regusername=request.POST.get('regusername', '')
            regpassword=request.POST.get('regpassword', '')
            regpassword2=request.POST.get('regpassword2', '')

            if regpassword==regpassword2:
                exts = users.objects.filter(username=regusername).exists()
                if exts == False:
                    user_obj = users(username=regusername, password=regpassword)
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

    else:
        form=RegisterForm()
    return render(request, 'mundialitisapps/index.html', {
    'form':form,
    })


#def post(request):
#    if request.method == 'POST':
#        form=UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('mundialitisapps/restaurant.html')
            #date = request.POST.get('date', '')
            #cost = request.POST.get('cost', '')
            #cost_obj = Cost(date = date, cost = cost)
            #cost_obj.save()
            #return HttpResponseRedirect(reverse('jobs:cost'))
#        else:
#            form= UserCreationForm()
#        return render(request, 'accounts/signup.html', {
#            'form':form,
#        })

def index2(request):
    return render(request, 'mundialitisapps/app.html')

def index3(request):
    return render(request, 'mundialitisapps/conference.html')


#def details(request, id, ttlscore):
#    if int(id)<31:
#        triv = questions.objects.get(id=id)
#        newid=int(id)+1
#        context={
#        'triv':triv,
#        'id': newid,
#        'ttlscore':ttlscore
#        }
#        return render(request, 'trivia/details.html', context)
#    else:
#        context={
#        'ttlscore':ttlscore
#        }
#        return render(request, 'trivia/scorescreen.html', context)


#def processing(request, option, id, ttlscore):
#    newid=int(id)+1
#    triv = questions.objects.get(id=id)
#    playeranswer=option
#    objanswer = answers.objects.get(id=id)
#    preanswer = objanswer.answer.replace(" ", "")
#    correctanswer = preanswer.replace(",", "")
#    questionscore = objanswer.score
#
#    if correctanswer == playeranswer:
#        context={
#        'triv': triv,
#        'message':'Respuesta Correcta',
#        'qscore':questionscore,
#        'ttlscore': int(ttlscore)+int(questionscore),
#        'id':newid
#        }
#        return render(request, 'trivia/outcome.html', context)
#    else:
#        context2={
#        'triv': triv,
#        'message':'Respuesta Incorrecta',
#        'qscore':0,
#        'ttlscore': ttlscore,
#        'id':newid
#        }
#        return render(request, 'trivia/outcome.html', context2)
