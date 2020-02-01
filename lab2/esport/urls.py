from django.conf.urls import url
from django.urls import path, include
from django.views import generic

from . import views
from .models import Player

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players/$', views.PlayerListView.as_view(), name='players'),
    url(r'^player/(?P<pk>\d+)$', views.PlayerDetailView.as_view(), name='player-detail'),

    url(r'^organizations/$', views.OrganizationListView.as_view(), name='organizations'),
    url(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='org-detail'),
]


