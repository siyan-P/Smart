from django import forms
from rest_framework import serializers
from listMed_app.models import MedModel
from django.contrib.auth.models import User

class MedicineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedModel
        fields = "__all__"
        
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']