from django import forms
from .models import teams, players


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


class TeamForm(forms.Form):
    POSICIONES_CHOICES = (
        ('arquero', 'ARQUERO'),
        ('defensa1', 'DEFENSA 1'),
        ('defensa2', 'DEFENSA 2'),
        ('defensa3', 'DEFENSA 3'),
        ('defensa4', 'DEFENSA 4'),
        ('centro1', 'CENTRO 1'),
        ('centro2', 'CENTRO 2'),
        ('centro3', 'CENTRO 3'),
        ('delantero1', 'DELANTERO 1'),
        ('delantero2', 'DELANTERO 2'),
        ('delantero3', 'DELANTERO 3'),
    )
    posiciones = forms.ChoiceField(choices=POSICIONES_CHOICES, widget=forms.RadioSelect, required=False)
    arquero = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    defensa1 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    defensa2 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    defensa3 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    defensa4 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    centro1 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    centro2 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    centro3 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    delantero1 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    delantero2 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    delantero3 = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'jugador'}))
    selecciones = forms.ModelChoiceField(queryset=teams.objects.all().order_by('pais'), required=False)
    jugadores = forms.ModelChoiceField(queryset=players.objects.all().order_by('nombre'), required=False)

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['posiciones'].widget.attrs = {
            'class': 'position'
        }
        self.fields['selecciones'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['jugadores'].widget.attrs = {
            'class': 'form-control'
        }
