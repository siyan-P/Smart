from rest_framework import serializers
from patientsapp.models import patientsModel

class PatientModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientsModel
        fields = "__all__"