
from rest_framework import serializers
from .models import Competencia, Convenio, Acuerdo, Edicto,  Flujograma, LeyesYDecreto


class CompetenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'

class LeyesYDecretoSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeyesYDecreto
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver

class ConvenioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver


class AcuerdoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Acuerdo
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver


class EdictoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edicto
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver




class FlujogramaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flujograma
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver


class ConvenioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver






