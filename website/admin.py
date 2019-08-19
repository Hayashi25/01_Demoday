from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Escola)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('data_requisicao',)

@admin.register(models.Aluno)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('data_criacao', 'data_atualizacao',)

@admin.register(models.Contato)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('data_mensagem',)