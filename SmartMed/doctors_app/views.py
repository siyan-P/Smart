from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.authtoken.models import 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from UserApp import models #importing token signals
from django.contrib.auth import login
from doctors_app.serializers import DrModelSerializer
from doctors_app.models import DrModel



@api_view(['POST',])
def registration_view(request):
    data = {}
    if request.method == 'POST':
        serializer = DrModelSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['res']='Account Created successful!'
            data['email'] = account.email
            data['token']=DrModel.objects.get(email=data['email']).token
            data['username'] = account.username
           
            return Response(data)
        
        else:
            return Response(serializer.errors)
        


@api_view(['POST',])
def login_doctor_view(request):
    if request.method == 'POST':
        ser_data =DrModelSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            print(ser_data)
            print(ser_data.cleaned_data.get('password'))
            if DrModel.objects.filter(username=data['username']).exists():
                data['password']=DrModel.objects.get(username=data['username']).password
                if data['password']==ser_data['password']:
                    
                    data['token']=DrModel.objects.get(email=data['email']).token
                    return Response(data['token'], status=status.HTTP_200_OK)
                return Response({'detail': 'password Invalid'})
            return Response({'detail': 'user does not exists'})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
