from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model = User
            fields = ['rol','username', 'password', 'nombre', 'email', 'apellido', 'fecha_nacimiento', 'direccion', 'ciudad',  'numero_telefonico']
