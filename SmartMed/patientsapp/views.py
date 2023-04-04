from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from patientsapp.models import patientsModel
from patientsapp.serializers import PatientModelSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

#add patient to db
class patientCreate(generics.CreateAPIView):
    queryset = patientsModel.objects.all()
    serializer_class = PatientModelSerializer
 
#retrive all the patients for each caretaker.  
@api_view(['GET'])
def PatientList(request):
    data = {}
    if request.method == 'GET':
        c_id = request.GET.get('c_id')
        #date=request.GET.get('date')
        data = patientsModel.objects.filter(c_id=c_id)
        if not data:
            return Response('No Patients Listed',status=status.HTTP_404_NOT_FOUND)
        serializer = PatientModelSerializer(data,many=True)
        data=serializer.data
            
    return Response(serializer.data)  
