from rest_framework import serializers

from authentication.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "is_staff",
            "is_superuser",
        )
