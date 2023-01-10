from rest_framework import serializers  
from rest_framework.views import View
from .models import CustomUser


class UserRegistrationsSerlizers(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=CustomUser
        fields=['email','name','password','password2','tc']
        extra_kwargs={
            'password':{'write_only':True}
        }


    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError('password and confirm \
            password doesnot match')

        return attrs


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)  


class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=CustomUser
        fields=['email','password']






