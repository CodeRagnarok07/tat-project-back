
from rest_framework import serializers
from .models import Noticia, GaleriaNoticia, HaciendoDiferencia, GaleriaHaciendoDiferencia, Congreso, GaleriaCongreso


#  NOTICIAS
class NoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class GaleriaNoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = GaleriaNoticia
        fields = ('imagen',)

class ViewNoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
    galeria = GaleriaNoticiaSerializers(many=True)




# Haciendo la diferencia
class HaciendoDiferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HaciendoDiferencia
        fields = '__all__'

class GaleriaHaciendoDiferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = GaleriaHaciendoDiferencia
        fields = ('imagen',)

class ViewHaciendoDiferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HaciendoDiferencia
        fields = '__all__'
    galeria = GaleriaHaciendoDiferenciaSerializers(many=True)


# congreso


# Haciendo la diferencia
class CongresoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Congreso
        fields = '__all__'

class GaleriaCongresoSerializers(serializers.ModelSerializer):
    class Meta:
        model = GaleriaCongreso
        fields = ('imagen',)

class ViewCongresoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Congreso
        fields = '__all__'
    galeria = GaleriaCongresoSerializers(many=True)
