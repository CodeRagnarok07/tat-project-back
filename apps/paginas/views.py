from .serializer import PaginaSerializers, SeccionSerializers, ContenidoSerializers
from .models import Pagina, Seccion, Contenido

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# api requeriments

# 1.- una lista de todas las paginas / como guia
class PaginasListView(APIView):
    def get(self, request, format=None):
        queryset = Pagina.objects.all()
        serializer = PaginaSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 2.- un endpoint que tome como parametro el nombre de la pagina y devuelva todos sus titulos y contenidos
class PaginaView(APIView):
    def get(self, request, page):

        queryset = Seccion.objects.filter(pagina=page).order_by("posicion")
        serializer = SeccionSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


