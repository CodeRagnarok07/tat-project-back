
from rest_framework import serializers
from .models import Oficina, Departamento, Equipo, Autoridad



class OficinaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = '__all__'

class DepartamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class EquipoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class AutoridadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autoridad
        fields = '__all__'









