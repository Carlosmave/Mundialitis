from django import forms
#from .models import Post
#class CostForm(forms.ModelForm):
class RegisterForm(forms.Form):
    #post = forms.CharField()
    regusername = forms.CharField()
    regpassword = forms.CharField()
    regpassword2 = forms.CharField()

class LoginForm(forms.Form):
    logusername = forms.CharField()
    logpassword = forms.CharField()


    #class Meta:
    #    model=Post
    #    fields = ('post',)

class PollaForm(forms.Form):
    apuesta = forms.CharField()