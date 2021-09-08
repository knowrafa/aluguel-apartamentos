from django.contrib import admin

# Register your models here.
from apartamentos.models import (
    ApartamentoModel,
    ApartamentoUsuarioModel,
)


@admin.register(ApartamentoModel)
class ApartamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(ApartamentoUsuarioModel)
class ApartamentoUsuarioAdmin(admin.ModelAdmin):
    pass
