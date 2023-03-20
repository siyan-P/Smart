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
from datetime import datetime
# from rest_framework import generics
# from rest_framework.generics import ListAPIView

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
            data['id']=account.id
            
            #return Response(data)
            return Response(data)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # if request.method == 
@api_view(['POST',])
def login_view(request):
    data = {}
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username =username,password=password )
        token,_=Token.objects.get_or_create(user=user)
        id = User.objects.get(username=username).id
    return Response({'token':token.key,'id':id})





        
     
        
       
        
        
     
        
        
    


        
        
