from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets


from django.db.models import Q

from core.pagination import CustomPagination, PaginationHandlerMixinApiView


from .models import Noticia, HaciendoDiferencia, Congreso

from .serializer import NoticiaSerializers,ViewNoticiaSerializers, CongresoSerializers, ViewCongresoSerializers, HaciendoDiferenciaSerializers, ViewHaciendoDiferenciaSerializers





class NoticiasListView(APIView, PaginationHandlerMixinApiView):
    """
    url: http://localhost:8000/publicaciones/resoluciones/
    """
    queryset = Noticia.objects.all().order_by("-fecha")
    serializer_class = NoticiaSerializers
    pagination_class = CustomPagination


    def get(self, request, format=None, *args, **kwargs):
        queryset = Noticia.objects.all().order_by("-fecha")
        search = request.GET.get('search', '')
        year = request.GET.get('year', '')
        if year:
            queryset = queryset.filter(fecha__year=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)


        return Response(serializer.data)

class NoticiaView(APIView):
    """
    url: http://127.0.0.1:8000/noticias/titulo
    """
    def get(self, request, slug):
        # queryset = get_object_or_404(Noticia, slug=slug )
        queryset = Noticia.objects.filter(slug=slug)
        serializer = ViewNoticiaSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HaciendoDiferenciasListView(APIView, PaginationHandlerMixinApiView):
    """
    url: http://localhost:8000/publicaciones/resoluciones/
    """
    queryset = HaciendoDiferencia.objects.all().order_by("-fecha")
    serializer_class = HaciendoDiferenciaSerializers
    pagination_class = CustomPagination


    def get(self, request, format=None, *args, **kwargs):
        queryset = HaciendoDiferencia.objects.all().order_by("-fecha")
        search = request.GET.get('search', '')
        year = request.GET.get('year', '')
        if year:
            queryset = queryset.filter(fecha__year=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)


        return Response(serializer.data)

class HaciendoDiferenciaView(APIView):
    """
    url: http://127.0.0.1:8000/HaciendoDiferencias/titulo
    """
    def get(self, request, slug):
        # queryset = get_object_or_404(HaciendoDiferencia, slug=slug )
        queryset = HaciendoDiferencia.objects.filter(slug=slug)
        serializer = ViewHaciendoDiferenciaSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CongresosListView(APIView, PaginationHandlerMixinApiView):
    """
    url: http://localhost:8000/publicaciones/resoluciones/
    """
    queryset = Congreso.objects.all().order_by("-fecha")
    serializer_class = CongresoSerializers
    pagination_class = CustomPagination


    def get(self, request, format=None, *args, **kwargs):
        queryset = Congreso.objects.all().order_by("-fecha")
        search = request.GET.get('search', '')
        year = request.GET.get('year', '')
        if year:
            queryset = queryset.filter(fecha__year=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)


        return Response(serializer.data)

class CongresoView(APIView):
    """
    url: http://127.0.0.1:8000/Congresos/titulo
    """
    def get(self, request, slug):
        # queryset = get_object_or_404(Congreso, slug=slug )
        queryset = Congreso.objects.filter(slug=slug)
        serializer = ViewCongresoSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




# Informes de Viajes Nacionales
# Edictos
# Convenios
# Acuerdos
# Leyes y Decretos
# combinando
