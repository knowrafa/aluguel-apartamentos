from django.shortcuts import render
from rest_framework import viewsets, mixins, views, renderers, generics


# Create your views here.
from rest_framework.response import Response

from apartamentos.filters.apartamento import ApartamentoFilter
from apartamentos.serializers import ApartamentoSerializer
from apartamentos.models import ApartamentoModel


class ApartamentoCreateView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "apartamento_create.html"
    permission_classes = []

    def get(self, request, *args, **kwargs):
        ap_serializer = ApartamentoSerializer()
        return Response(data={"serializer": ap_serializer})


class ApartamentoTemplateView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "index.html"
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        payload = {
            "table_headers": [
                "Setor",
                "Valor",
                "Elevador",
                "Vaga",
                "Condomínio",
                "Contato",
                "Link",
            ],
            "apartamentos": ApartamentoModel.objects.all(),
        }
        return Response(data=payload)

    def post(self, request):
        return Response()


class ApartamentoViewSet(
    viewsets.ModelViewSet,
):
    queryset = ApartamentoModel.objects.all()
    serializer_class = ApartamentoSerializer
    filter_class = ApartamentoFilter
