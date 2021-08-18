from rest_framework import serializers

from apartamentos.models import ApartamentoModel, ApartamentoUsuarioModel
from authentication.serializers.user import UsuarioSerializer


class ApartamentoUsuarioSerializer(serializers.ModelSerializer):
    usuarios = UsuarioSerializer(required=False)

    class Meta:
        model = ApartamentoUsuarioModel
        fields = ("id", "usuarios", "envio_email", "envio_sms")


class ApartamentoSerializer(serializers.ModelSerializer):
    cuidadores = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        required=False,
        write_only=True,
    )

    class Meta:
        model = ApartamentoModel
        fields = (
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
            "vaga",
            "elevador",
            "link",
            "contato",
            "cuidadores",
        )

    def create(self, validated_data):
        return super(ApartamentoSerializer, self).create(validated_data)

    def to_representation(self, instance):
        obj = super(ApartamentoSerializer, self).to_representation(instance)
        obj["cuidadores"] = [
            ApartamentoUsuarioSerializer(
                ApartamentoUsuarioModel.objects.get(apartamento=instance, usuarios=pessoa),
                context=self.context,
            ).data
            for pessoa in instance.pessoas.all()
        ]
        return obj
