from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_auth.serializers import LoginSerializer

class RegisterSerializer(serializers.ModelSerializer):
    """
    Generates Serializer fields based on the database Model .
    ModelSerializer is a subclass of serializers.
    """
    class Meta:            
        model=User        
        fields=[     'id',
                'first_name',
                'last_name', 
                'date_of_birth',
                'username',
                'password',
                'email', 
                'phone', 
                'street', 
                'zip_code', 
                'city',
                'state', 
                'country', 
            ]
        
        
    def create(self,validated_data):
        """
        To hide password values ,here Convert password into hash values.
        """ 
        validated_data["password"]=make_password(validated_data["password"])
        return super().create(validated_data)

class LoginSerializer(LoginSerializer):
    """
    Define Serializer class for custemization in Login-view
    """
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50,style={'input_type': 'password'})
