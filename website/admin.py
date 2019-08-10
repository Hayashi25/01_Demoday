from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Escola)
admin.site.register(models.Aluno)

@admin.register(models.Contato)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('data_mensagem',)