
from rest_framework import serializers
from .models import Resolucion, CategoriasResoluciones, PonenciasArchivos, Ponencia, RevistasTributaria, Memorias, Otros


class CategoriasResolucionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriasResoluciones
        fields = ('titulo',)


class ResolucionSerializers(serializers.ModelSerializer):

    # def is_named_bar(self):
    #     return self.ver == "bar"
    ver = serializers.SerializerMethodField(source='ver')
    categoria = serializers.SerializerMethodField(source='categoria')

    class Meta:
        model = Resolucion
        fields = ('titulo', 'año', 'categoria', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver

    def get_categoria(self, obj):
        return obj.categoria


class EntradasPonenciasSerializers(serializers.ModelSerializer):
    class Meta:
        model = PonenciasArchivos
        # fields = '__all__'

        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver

class PonenciasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ponencia
        fields = '__all__'
    archivos = EntradasPonenciasSerializers(many=True)


class RevistasTributariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = RevistasTributaria
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver


class MemoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Memorias
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver

class OtrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = ('titulo', 'ver', 'descargar')

    def get_ver(self, obj):
        return obj.ver

    def get_descargar(self, obj):
        return obj.ver