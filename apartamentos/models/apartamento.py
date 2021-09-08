from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

# Create your models here.
from utils.mixins.models import SetUpModel


class ApartamentoModel(SetUpModel):
    setor = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    valor = models.PositiveIntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    nota = models.FloatField(
        null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    # incluso = models.TextField(null=True, blank=True)

    condominio = models.PositiveIntegerField(null=True, blank=True)
    iptu = models.PositiveIntegerField(null=True, blank=True)
    andar = models.PositiveIntegerField(null=True, blank=True)
    area = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Área em m²"),
    )
    quantidade_quartos = models.PositiveIntegerField(null=True, blank=True)
    quantidade_banheiros = models.PositiveIntegerField(null=True, blank=True)
    vaga = models.BooleanField(default=False)
    elevador = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)
    contato = models.CharField(max_length=255, null=True, blank=True)

    pessoas = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="ApartamentoUsuarioModel",

    )


class ApartamentoUsuarioModel(SetUpModel):
    apartamento = models.ForeignKey(
        "ApartamentoModel",
        related_name="apartamentos_usuarios",
        on_delete=models.CASCADE,
    )

    usuarios = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="apartamentos_usuarios",
        on_delete=models.CASCADE,
    )

    envio_sms = models.BooleanField(default=True)

    envio_email = models.BooleanField(default=True)
