from django import forms
from .models import users
#class CostForm(forms.ModelForm):
class RegisterForm(forms.Form):
    #post = forms.CharField()
    regusername = forms.CharField()
    regpassword = forms.CharField()
    regpassword2 = forms.CharField()

class LoginForm(forms.Form):
    logusername = forms.CharField()
    logpassword = forms.CharField()

class LobbyForm(forms.Form):
    lobbyname = forms.CharField()
    lobbypassword = forms.CharField()


    #class Meta:
    #    model=Post
    #    fields = ('post',)


    #invitacion
class invit(forms.Form):
	grupo = forms.CharField(widget=forms.TextInput(), required=True);
	usuario = forms.CharField(widget=forms.TextInput(),required=True)

class UserForm(forms.ModelForm):
    class Meta:
            model = users
            fields = ['username', 'password']
