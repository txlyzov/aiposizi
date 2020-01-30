from django.contrib import admin

# Register your models here.

from .models import Player, Race, Country, Organization

admin.site.register(Player)
admin.site.register(Organization)
admin.site.register(Country)
admin.site.register(Race)
