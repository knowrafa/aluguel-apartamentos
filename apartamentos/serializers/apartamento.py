from rest_framework import serializers

from apartamentos.models import ApartamentoModel, ApartamentoUsuarioModel
from authentication.serializers.user import UsuarioSerializer


class ApartamentoUsuarioSerializer(serializers.ModelSerializer):
    usuarios = UsuarioSerializer(required=False)

    class Meta:
        model = ApartamentoUsuarioModel
        fields = ("id", "usuarios", "envio_email", "envio_sms")


class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartamentoModel
        fields = (
            "id",
            "setor",
            "endereco",
            "valor",
            "descricao",
            "nota",
            "incluso",
            "condominio",
            "iptu",
            "andar",
            "area",
            "quantidade_quartos",
            "quantidade_banheiros",
            "elevador",
            "vaga",
            "link",
            "contato",
        )


