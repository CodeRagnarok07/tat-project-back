
from rest_framework import serializers
from .models import Pagina, Seccion, Contenido



class PaginaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagina
        fields = '__all__'

class ContenidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = '__all__'


class SeccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'
    contenido = ContenidoSerializers(many=True)
    


