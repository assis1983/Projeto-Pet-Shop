from rest_framework.serializers import ModelSerializer
from reserva.models import Reserva, Petshop

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopNestedModelSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'