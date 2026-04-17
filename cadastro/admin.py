# cadastro\admin.py

from django.contrib import admin
from .models import Contato, Pessoa, Telefone

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['numero', 'pessoa']    


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'assunto']     

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Contato, ContatoAdmin)