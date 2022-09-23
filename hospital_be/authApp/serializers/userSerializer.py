from rest_framework import serializers
from authApp.models.user import User
from authApp.models.medico import Medico
from authApp.serializers.medicoSerializer import MedicoSerializer
from authApp.models.paciente import Paciente
from authApp.serializers.pacienteSerializer import PacienteSerializer


class UserSerializer(serializers.ModelSerializer):
      Medico = MedicoSerializer()
      class Meta:
            model = User
            fields = ['id', 'rol','username', 'password', 'nombre', 'email', 'apellido', 'fecha_nacimiento', 'direccion', 'ciudad',  'numero_telefonico']
      def create(self, validated_data):
            medicoData = validated_data.pop('Medico')
            userInstance = User.objects.create(**validated_data)
            Medico.objects.create(user=userInstance, **medicoData)
            return userInstance

def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      medico = medico.objects.get(user=obj.id)
      return {
                  'id': user.id,
                  'rol': user.rol,
                  'username': user.username,
                  'nombre': user.nombre,
                  'email': user.email,
                  "apellido": user.apellido,
                  "fecha_nacimiento": user.fecha_nacimiento,
                  "direccion": user.direccion,
                  "ciudad": user.ciudad,
                  "numero_telefonico": user.numero_telefonico,
      }


class UserSerializer(serializers.ModelSerializer):
      Paciente = PacienteSerializer()
      class Meta:
            model = User
            fields = ['id', 'rol','username', 'password', 'nombre', 'email', 'apellido', 'fecha_nacimiento', 'direccion', 'ciudad',  'numero_telefonico']
      def create(self, validated_data):
            pacienteData = validated_data.pop('Paciente')
            userInstance = User.objects.create(**validated_data)
            Paciente.objects.create(user=userInstance, **pacienteData)
            return userInstance

def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      paciente = paciente.objects.get(user=obj.id)
      return {
                  'id': user.id,
                  'rol': user.rol,
                  'username': user.username,
                  'nombre': user.nombre,
                  'email': user.email,
                  "apellido": user.apellido,
                  "fecha_nacimiento": user.fecha_nacimiento,
                  "direccion": user.direccion,
                  "ciudad": user.ciudad,
                  "numero_telefonico": user.numero_telefonico,
                  
      }