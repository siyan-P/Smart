# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
    data={}
    if request.method == 'POST':
        username=request.data.get("username")
        password=request.data.get("password")
        try:
            data['username']=DrModel.objects.get(username=username).username
            data['email']=DrModel.objects.get(username=username).email
            if password==DrModel.objects.get(username=username).password:
                data['token']=DrModel.objects.get(email=data['email']).token
                return Response(data['token'], status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'password Invalid'},status=status.HTTP_400_BAD_REQUEST)
           
        except DrModel.DoesNotExist:
            return Response({'detail':'Invalid Username'},status=status.HTTP_400_BAD_REQUEST)
           
                
        
       