from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class UserRegistrationviews(APIView):

    def post(self,request,formate=None):
        return Response({'mesg':'created success'})

