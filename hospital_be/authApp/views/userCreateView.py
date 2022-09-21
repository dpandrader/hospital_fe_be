from rest_framework import status, views

from django.http.response import JsonResponse
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.models.user import User
import json

class UserCreateView(views.APIView):
      def post(self, request, *args, **kwargs):
            #serializer = UserSerializer(data=request.data)
            #serializer.is_valid(raise_exception=True)
            #serializer.save()
            #tokenData = {"username":request.data["username"],
          #"password":request.data["password"]}
            #tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            #tokenSerializer.is_valid(raise_exception=True)
            
            #return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
            jd=json.loads(request.body)
            User.objects.create(id=jd["id"],username=jd["username"],password=jd["password"],name=jd["name"],email=jd["email"],lastname=jd["lastname"],birth_date=jd["birth_date"],address=jd["address"],city=jd["city"],telephone_number=jd["telephone_number"],account=jd["account"])
            datos={"message":"Success"}
            return JsonResponse(datos)