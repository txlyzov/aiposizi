from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Organization, Player, Country, Race


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_organisations = Organization.objects.all().count()
    num_undead_players = Player.objects.filter(race__name__contains='Un').count()
    num_orc_players = Player.objects.filter(race__name__contains='Or').count()
    num_ne_players = Player.objects.filter(race__name__contains='NE').count()
    num_human_players = Player.objects.filter(race__name__contains='Hu').count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_organisations': num_organisations,
                 'num_undead_players': num_undead_players,
                 'num_ne_players': num_ne_players,
                 'num_human_players': num_human_players,
                 'num_orc_players': num_orc_players},
    )


class PlayerListView(generic.ListView):
    model = Player


class PlayerDetailView(generic.DetailView):
    model = Player


class OrganizationListView(generic.ListView):
    model = Organization


class OrganizationDetailView(generic.DetailView):
    model = Organization
