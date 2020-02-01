from django.conf.urls import url
from django.urls import path, include
from django.views import generic

from . import views
from .models import Player

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players/$', views.PlayerListView.as_view(), name='players'),
    url(r'^player/(?P<pk>\d+)$', views.PlayerDetailView.as_view(), name='player-detail'),
<<<<<<< HEAD
    url(r'^player/create/$', views.PlayerCreate.as_view(), name='player-create'),
    url(r'^player/(?P<pk>\d+)/update/$', views.PlayerUpdate.as_view(), name='player-update'),
    url(r'^player/(?P<pk>\d+)/delete/$', views.PlayerDelete.as_view(), name='player-delete'),
=======

    url(r'^organizations/$', views.OrganizationListView.as_view(), name='organizations'),
    url(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='org-detail'),
>>>>>>> f67f7220c05e1dd22478e989dcfe6f7aa7c9f18e
]


