from .models import User
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
            'communication_tool',
            'introduction',
            'native_languages',
            'learning_languages',
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
    