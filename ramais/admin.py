from django.contrib import admin

from .models import Ramal, Departamento

@admin.register(Ramal)
class RamalAdmin(admin.ModelAdmin):
    list_display = ('setor', 'localizacao', 'responsavel', 'telefone')

#@admin.register(Departamento)
#class DepartamentoAdmin(admin.ModelAdmin):
    #list_display = ('setor',)
