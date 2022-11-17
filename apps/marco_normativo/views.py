from django.shortcuts import render

# Create your views here.







from django.db.models import Q

from core.pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import FileResponse

from .models import Competencia, Convenio, Acuerdo, Edicto,  Flujograma, LeyesYDecreto

from .serializer import CompetenciaSerializers, ConvenioSerializers,AcuerdoSerializers,EdictoSerializers,FlujogramaSerializers,LeyesYDecretoSerializers

from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class CompetenciasList(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/resoluciones/
    """
    serializer_class = CompetenciaSerializers
    pagination_class = CustomPagination
    queryset = Competencia.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = Competencia.objects.all().order_by("-pk")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ConveniosViewSet(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/Convenioes/
    """
    serializer_class = ConvenioSerializers
    pagination_class = CustomPagination
    queryset = Convenio.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = Convenio.objects.all().order_by("-pk")

        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        if year:
            queryset = queryset.filter(año=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Convenio, pk=pk )
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.archivo.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.archivo.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.archivo.name

        return response


class AcuerdosViewSet(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/Acuerdoes/
    """
    serializer_class = AcuerdoSerializers
    pagination_class = CustomPagination
    queryset = Acuerdo.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = Acuerdo.objects.all().order_by("-pk")

        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        if year:
            queryset = queryset.filter(año=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Acuerdo, pk=pk )
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.archivo.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.archivo.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.archivo.name

        return response


class EdictosViewSet(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/Edictoes/
    """
    serializer_class = EdictoSerializers
    pagination_class = CustomPagination
    queryset = Edicto.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = Edicto.objects.all().order_by("-pk")

        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        if year:
            queryset = queryset.filter(año=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Edicto, pk=pk )
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.archivo.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.archivo.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.archivo.name

        return response


class FlujogramasViewSet(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/Flujogramaes/
    """
    serializer_class = FlujogramaSerializers
    pagination_class = CustomPagination
    queryset = Flujograma.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = Flujograma.objects.all().order_by("-pk")

        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        if year:
            queryset = queryset.filter(año=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Flujograma, pk=pk )
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.archivo.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.archivo.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.archivo.name

        return response


class LeyesYDecretosViewSet(viewsets.ModelViewSet):
    """
    url: http://localhost:8000/publicaciones/LeyesYDecretoes/
    """
    serializer_class = LeyesYDecretoSerializers
    pagination_class = CustomPagination
    queryset = LeyesYDecreto.objects.all().order_by("-pk")

    def list(self, request, format=None, *args, **kwargs):
        queryset = LeyesYDecreto.objects.all().order_by("-pk")

        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        if year:
            queryset = queryset.filter(año=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search))

        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(LeyesYDecreto, pk=pk )
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.archivo.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.archivo.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.archivo.name

        return response




