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

@api_view(['PATCH'])
def update_nfc(request):
    if request.method == 'PATCH':
       id = request.GET.get('id')
       data = patientsModel.objects.get(id=id)
       nfc_id = request.GET.get('nfc_id')
       nid=  patientsModel.objects.get(id=id).nfc_id
       fdata = patientsModel.objects.all()
       serializer =  PatientModelSerializer(fdata,many=True)
       fdata=serializer.data
       if not nid:
           for d in fdata:
               if d['nfc_id'] == nfc_id:
                   print('not possible to')
                   return Response('Tag alreday Registered With another Patient',status=status.HTTP_405_METHOD_NOT_ALLOWED)
           data.nfc_id = nfc_id
           data.save()
           return Response('Sucessfully updated')
       else :
           return Response('Patient already registered with tag',status=status.HTTP_405_METHOD_NOT_ALLOWED)
       
class patientInd(generics.RetrieveAPIView):
    queryset = patientsModel.objects.all()
    serializer_class = PatientModelSerializer            
    