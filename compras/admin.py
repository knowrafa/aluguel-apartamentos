from django.contrib import admin

# Register your models here.
from apartamentos.models import (
    ApartamentoModel,
    ApartamentoUsuarioModel,
    Treino,
    Musculacao,
    Aerobico,
)


@admin.register(ApartamentoModel)
class ApartamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(ApartamentoUsuarioModel)
class ApartamentoUsuarioAdmin(admin.ModelAdmin):
    pass


# @admin.register(Treino)
# class TreinoAdmin(admin.ModelAdmin):
#     pass


@admin.register(Musculacao)
class MusculacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Aerobico)
class AerobicoAdmin(admin.ModelAdmin):
    pass
