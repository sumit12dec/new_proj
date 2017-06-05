from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'role')
