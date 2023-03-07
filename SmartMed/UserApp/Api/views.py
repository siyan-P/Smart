from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from UserApp import models #importing token signals
from django.contrib.auth import login
from UserApp.Api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    data = {}
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['res']='Account Created successful!'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key 
            data['token']=token
            #return Response(data)
            return Response({'detail': 'Account Created!'},status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
