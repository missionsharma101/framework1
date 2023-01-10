from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from apps.project.serilizer import *


class UserRegistrationviews(APIView):
    def post(self, request, formate=None):
        serializer = UserRegistrationsSerlizers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"msg": "Registration success"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserloginView(APIView):
    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({"msg": "login success"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": {"non_field_errors": ["email or password is not valid"]}},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response({"msg": "error"}, status=status.HTTP_200_OK)
