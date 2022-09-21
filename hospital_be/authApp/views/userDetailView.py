from rest_framework import status, views

from django.http.response import JsonResponse
#from rest_framework_simplejwt.backends import TokenBackend
from authApp.models.user import User
import json

class UserDetailView(views.APIView):
      #queryset = User.objects.all()
      #serializer_class = UserSerializer
      #permission_classes = (IsAuthenticated,)
      def get(self, request, id=0, *args, **kwargs):

          #token = request.META.get('HTTP_AUTHORIZATION')[7:]
          #tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
          #valid_data = tokenBackend.decode(token,verify=False)
          #if valid_data['user_id'] != kwargs['pk']:
          #  stringResponse = {'detail':'Unauthorized Request'}
          #  return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
          #return super().get(request, *args, **kwargs)
          if (id > 0):
              usuarios = list(User.objects.filter(id=id).values())
              if len(usuarios)>0:
                  User= usuarios[0]
                  datos={"message":"Success","User":User}
              else:
                  datos={"messaje":"User not found..."}
              return JsonResponse(datos)
          else:
              usuarios= list(User.objects.values())
              if len(usuarios)>0:
                  datos= {"message":"Success", "usuarios": usuarios}
              else:
                  datos={"message":"usuarios not found..."}
          
              return JsonResponse(datos)