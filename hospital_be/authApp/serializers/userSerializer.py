from rest_framework import serializers
from authApp.models.user import User
from authApp.models.account import Account
from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
      account = AccountSerializer()
      class Meta:
            model = User
            fields = ['id', 'username', 'password', 'name', 'email', 'lastname', 'birth_date', 'address', 'city',  'telephone_number', 'account']
      def create(self, validated_data):
            accountData = validated_data.pop('account')
            userInstance = User.objects.create(**validated_data)
            Account.objects.create(user=userInstance, **accountData)
            return userInstance

def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      account = Account.objects.get(user=obj.id)
      return {
                  'id': user.id,
                  'username': user.username,
                  'name': user.name,
                  'email': user.email,
                  "lastname": user.lasname,
                  "birth_date": user.birth_date,
                  "address": user.addres,
                  "city": user.city,
                  "telephone_number": user.telephone_number,
                  'account': {
                        'id': account.id,
                        'balance': account.balance,
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                  }
}