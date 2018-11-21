from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    fields = ['input', 'output', 'creation_date']
    list_display = ('creation_date', 'input', 'output')

admin.site.register(Game, GameAdmin)
