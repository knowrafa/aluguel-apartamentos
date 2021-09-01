from django.db import models
from utils.mixins.models import SetUpModel
from django.utils.html import mark_safe


class TipoItemModel(SetUpModel):
    nome = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)

    @property
    def icone_tag(self):
        return mark_safe(f"{self.icone}")

    def __str__(self):
        return self.nome


class ItemCompraModel(SetUpModel):
    compra = models.ForeignKey(
        "CompraModel", related_name="itens", on_delete=models.CASCADE
    )
    tipo = models.ForeignKey(
        "TipoItemModel", related_name="itens", on_delete=models.CASCADE
    )


class CompraModel(SetUpModel):
    valor_total = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "compras"
