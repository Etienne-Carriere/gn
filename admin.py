from django.contrib import admin

from .models import *

class JoueurAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_name')

class PisteAdmin(admin.ModelAdmin):
    list_display = ('letter', 'title')

class EnqueteAdmin(admin.ModelAdmin):
    list_display = ('piste', 'joueur', 'niveau')

class InterceptionAdmin(admin.ModelAdmin):
    list_display = ('origin','target','resultat','done')

admin.site.register(Joueur,JoueurAdmin)
admin.site.register(Piste,PisteAdmin)
admin.site.register(Enquete,EnqueteAdmin)
admin.site.register(Interception,InterceptionAdmin)
