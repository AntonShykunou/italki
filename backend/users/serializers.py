from .models import User, CommunicationTool
from rest_framework import serializers
from locations.serializers import CitySerializer

class UserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    city = CitySerializer()
    
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'city',
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
    photo = serializers.ImageField(max_length=None, use_url=True)
    city = CitySerializer()

    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'city',
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
    