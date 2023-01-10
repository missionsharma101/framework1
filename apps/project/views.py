from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .renders import UserRender
from django.contrib.auth import authenticate
from apps.project.serilizer import *
from rest_framework.permissions import IsAuthenticated


# Generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationviews(APIView):
    renderer_classes = [UserRender]

    def post(self, request, formate=None):
        serializer = UserRegistrationsSerlizers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            form = serializer.save()
            token = get_tokens_for_user(form)

            return Response(
                {"token": token, "msg": "Registration success"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserloginView(APIView):
    renderer_classes = [UserRender]

    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"token": token, "msg": "login success"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": {"non_field_errors": ["email or password is not valid"]}},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response({"msg": "error"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    renderer_classes=[UserRender]
    permission_classes=[IsAuthenticated]

    def get(self,request,formate=None):
        serializer=UserProfileSerilizer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)


class UserChangePassword(APIView):
    renderer_classes=[UserRender]
    permission_classes=[IsAuthenticated]

    def post(self, request, formate=None ):
        serializer=UserChangePassSerializer(data=request.data,context={'user':request.user})

        if serializer.is_valid(raise_exception=True):
            return Response({'mesg':"password change"},status=status.HTTP_200_OK)
            

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
