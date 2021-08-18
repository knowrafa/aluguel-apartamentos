from django.db import models


class Treino(models.Model):
    tempo = models.PositiveIntegerField(null=True, blank=True)
    nome = models.PositiveIntegerField(null=True, blank=True)
    plano = models.ForeignKey(
        "ApartamentoModel", on_delete=models.CASCADE
    )


    class Meta:
        abstract = True


class Musculacao(Treino):
    intervalo = models.CharField(max_length=255, null=True, blank=True)


class Aerobico(Treino):
    esteira = models.BooleanField(default=False)
