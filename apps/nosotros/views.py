
# Create your views here.
from django.shortcuts import get_object_or_404
from .serializer import OficinaSerializers, DepartamentoSerializers, AutoridadSerializers, EquipoSerializers
from .models import Oficina, Departamento, Autoridad, Equipo

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class OficinaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Oficina.objects.all().order_by("-order")
        serializer = OficinaSerializers(queryset, many=True)
        return Response(serializer.data)

class DepartamentoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Departamento.objects.all()#.order_by("-order")
        serializer = DepartamentoSerializers(queryset, many=True)
        return Response(serializer.data)



class AutoridadViewSet(viewsets.ViewSet):
    serializer_class = AutoridadSerializers
    queryset = Autoridad.objects.all().order_by("-pk")
    def list(self, request, format=None, *args, **kwargs):
        queryset = Autoridad.objects.all()#.order_by("-order")
        serializer = AutoridadSerializers(queryset, many=True)
        return Response(serializer.data)

class AutoridadDetail(APIView):
    def get(self, request, slug=None):
        current = get_object_or_404(Autoridad, slug=slug)
        serializer = AutoridadSerializers(current)
        return Response(serializer.data)



class EquipoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Equipo.objects.all()#.order_by("-order")
        serializer = EquipoSerializers(queryset, many=True)
        return Response(serializer.data)

class EquipoDetail(APIView):
    def get(self, request, slug=None):
        current = get_object_or_404(Equipo, slug=slug)
        serializer = EquipoSerializers(current)
        return Response(serializer.data)