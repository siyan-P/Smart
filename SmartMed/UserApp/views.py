from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from UserApp.Api.serializers import RegistrationSerializer
from rest_framework import generics

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
class UserInd(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
