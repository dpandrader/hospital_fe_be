from authApp.models.medico import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id','user','especialidad']