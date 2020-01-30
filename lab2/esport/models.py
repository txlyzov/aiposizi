from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class Race(models.Model):
    """
    Model represent a game race (e.g. Orc, Undead, Human, Night elf)
    """
    RACES = (
        ('Hu', 'Human'),
        ('Or', 'Orc'),
        ('Un', 'Undead'),
        ('NE', 'Night Elf'),
    )

    name = models.CharField(max_length=2, choices=RACES, help_text="Race")

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    Model represent a country
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
    Model represent a organization that purchase players
    """
    name = models.CharField(max_length=20)
    location = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('org-detail', args=[str(self.id)])


class Player(models.Model):
    """
    Model represent a player
    """
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    birth = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('player-detail', args=[str(self.id)])
