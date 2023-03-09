from django import forms
from rest_framework import serializers
from listMed_app.models import MedModel

class MedicineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedModel
        fields = "__all__"