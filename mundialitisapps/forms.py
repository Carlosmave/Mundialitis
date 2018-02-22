from django import forms

class RegisterForm(forms.Form):
    regusername = forms.CharField()
    regpassword = forms.CharField()
    regpassword2 = forms.CharField()

class CompleteRegForm(forms.Form):
    regfirstname = forms.CharField()
    reglastname = forms.CharField()
    regemail = forms.CharField()
    regaddress = forms.CharField()
    regcountry = forms.CharField()
    regmoney = forms.IntegerField()


class LoginForm(forms.Form):
    logusername = forms.CharField()
    logpassword = forms.CharField()

class LobbyForm(forms.Form):
    lobbyname = forms.CharField()
    lobbypassword = forms.CharField()
    lobbymoney = forms.IntegerField()
