from datetime import timedelta

import django_filters

from apartamentos.models import ApartamentoModel
from utils.handlers.date import parse_date_to_iso


class ApartamentoFilter(django_filters.FilterSet):
    dia = django_filters.CharFilter(method="filter_dia")

    class Meta:
        model = ApartamentoModel
        fields = ("dia",)

    def filter_dia(self, queryset, name, value):

        data_inicio = parse_date_to_iso(value).astimezone()
        data_fim = data_inicio + timedelta(days=1)

        return queryset.filter(criado_em__range=[data_inicio, data_fim])
