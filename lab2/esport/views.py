from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Player
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


class PlayerCreate(CreateView):
    model = Player
    fields = ['nickname','name','birth', 'country']


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['nickname', 'race', 'team']


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('players')
