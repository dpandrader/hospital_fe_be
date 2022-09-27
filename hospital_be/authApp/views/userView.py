from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.backends import TokenBackend
#from rest_framework.permissions import IsAuthenticated
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserListaView(generics.ListAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
      #permission_classes = (IsAuthenticated,)

      def list(self, request):
        print("GET a todos los Usuario")
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
      
class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
      lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
      lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
      #permission_classes = (IsAuthenticated,)
      
      def get(self, request, *args, **kwargs):
          print("GET a Usuario")
          """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
          return super().get(request, *args, **kwargs)

      def put(self, request, *args, **kwargs):
          print("PUT a Usuario")
          """ if valid_data['user_id'] != kwargs['pk']:
              stringResponse = {'detail':'Unauthorized Request'}
              return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
          return super().put(request, *args, **kwargs)

      def delete(self, request, *args, **kwargs):
          print("DELETE a Usuario")
          """ if valid_data['user_id'] != kwargs['pk']:
              stringResponse = {'detail':'Unauthorized Request'}
              return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
          return super().delete(request, *args, **kwargs)