from django import forms
#from .models import Post
#class CostForm(forms.ModelForm):
class RegisterForm(forms.Form):
    #post = forms.CharField()
    regusername = forms.CharField()
    regpassword = forms.CharField()
    regpassword2 = forms.CharField()
    #class Meta:
    #    model=Post
    #    fields = ('post',)
