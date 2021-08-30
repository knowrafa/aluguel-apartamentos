"""podcast_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from rest_framework_nested import routers
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

from apartamentos import views

router = routers.DefaultRouter()

router.register("apartamentos", views.ApartamentoViewSet, basename="apartamentos")


app_name = "apartamentos"


# Apartamento Urls
urlpatterns = [
    path(
        "", RedirectView.as_view(url=reverse_lazy("apartamentos:listar-apartamentos"))
    ),
    path("api/", include(router.urls)),
    path(
        "apartamentos/create/",
        views.ApartamentoCreateView.as_view(),
        name="criar-apartamento",
    ),
    path(
        "apartamentos/",
        views.ApartamentoTemplateView.as_view(),
        name="listar-apartamentos",
    ),
    path(
        "apartamentos/<uuid:pk>/",
        views.ApartamentoRetrieveView.as_view(),
        name="retrieve-apartamentos",
    ),
    path(
        "apartamentos/delete/<uuid:pk>/",
        views.ApartamentoDeleteView.as_view(),
        name="deletar-apartamento",
    ),
    path(
        "apartamentos/update/<uuid:pk>/",
        views.ApartamentoUpdateView.as_view(),
        name="atualizar-apartamento",
    ),
]
