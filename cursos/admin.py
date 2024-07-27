from django.contrib import admin

from .models import Avaliacao, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        'curso',
        'nome',
        'email',
        'criacao',
        'atualizacao',
        'ativo',
    )
