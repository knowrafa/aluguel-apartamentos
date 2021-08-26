from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins, views, renderers, generics


# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apartamentos.filters.apartamento import ApartamentoFilter
from apartamentos.serializers import ApartamentoSerializer
from apartamentos.models import ApartamentoModel


class ApartamentoDeleteView(views.APIView):
    permission_classes = []
    queryset = ApartamentoModel.objects.all()

    def post(self, request, *args, **kwargs):
        obj = self.queryset.get(pk=kwargs.get("pk"))
        obj.delete()
        return redirect("apartamentos:listar-apartamentos")


class ApartamentoRetrieveView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "apartamento_retrieve.html"
    permission_classes = []
    queryset = ApartamentoModel.objects.all()
    serializer_class = ApartamentoSerializer

    def get(self, request, *args, **kwargs):
        obj = self.queryset.get(pk=kwargs.get("pk"))
        apartamento_serializer = self.serializer_class(instance=obj)
        return Response(
            {
                "serializer": apartamento_serializer,
            }
        )


class ApartamentoUpdateView(views.APIView):
    permission_classes = []
    queryset = ApartamentoModel.objects.all()
    serializer_class = ApartamentoSerializer

    def post(self, request, *args, **kwargs):
        obj = self.queryset.get(pk=kwargs.get("pk"))
        apartamento_serializer = self.serializer_class(instance=obj, data=request.data)
        if apartamento_serializer.is_valid():
            apartamento_serializer.save()
            return redirect("apartamentos:listar-apartamentos")
        return Response({"serializer": apartamento_serializer})


class ApartamentoCreateView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "apartamento_create.html"
    permission_classes = []

    def get(self, request, *args, **kwargs):
        ap_serializer = ApartamentoSerializer()
        return Response(data={"serializer": ap_serializer})

    def post(self, request, *args, **kwargs):
        apartamento_serializer = ApartamentoSerializer(data=request.data)
        if apartamento_serializer.is_valid():
            apartamento_serializer.save()

        return Response(
            data={
                "serializer": apartamento_serializer,
                "errors": apartamento_serializer.errors
                if apartamento_serializer.errors
                else None,
            }
        )


class ApartamentoTemplateView(views.APIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "listar_apartamentos.html"
    # authentication_classes = []
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
