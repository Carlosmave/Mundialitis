# -*- coding: utf-8 -*-
from django.http import JsonResponse

from .models import Player, Team


def get_players(request):
    pais_id = request.GET.get('pais_id')
    jugadores_select = '<option value="" selected="selected">---------</option>'
    if pais_id:
        pais = Team.objects.get(pk=pais_id)
        jugadores = Player.objects.filter(pais=pais).order_by('nombre')
        for jugador in jugadores:
            jugadores_select += '<option value="%s">%s</option>' % (
                jugador.id,
                jugador.nombre
            )
    response = {}
    response['jugadores'] = jugadores_select
    return JsonResponse(response)
