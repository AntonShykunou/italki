from .models import User, CommunicationTool
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'photo',
            'introduction',
            'last_visit'
        )

class CommunicationToolSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    
    class Meta:
        model = CommunicationTool
        fields = (
            'name',
            'address',
            'user' 
        )

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'photo',
            'introduction',
            'last_visit'
        )
    

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'password'
        )
        
        extra_kwargs = {
            'password': {'write_only': True}
        }

   
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    