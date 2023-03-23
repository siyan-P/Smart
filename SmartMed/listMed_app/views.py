from rest_framework.response import Response
from listMed_app.serializers import MedicineSerializer,Userserializer
from rest_framework import generics
from listMed_app.models import MedModel
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.
class MedicineView(generics.CreateAPIView):
   queryset = MedModel.objects.all()
   serializer_class = MedicineSerializer
   

#from .models import Post
#from .serializers import PostSerializer


@api_view(['GET'])
def UserPostListView(request):
    data = {}
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        date=request.GET.get('date')
        data = MedModel.objects.filter(user_id=user_id)
        if not data:
            return Response('User not found',status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineSerializer(data,many=True)
        data=serializer.data
        
        dates=datetime.strptime(date, '%Y-%m-%d')
        filterdData = []
        for i in data:
            currentDate = datetime.strptime(i['startDate'][:10],'%Y-%m-%d')
            if currentDate == dates:
                filterdData.append(i)
        if not filterdData:
            return Response('data not found',status=status.HTTP_404_NOT_FOUND)
            
    return Response(filterdData)

#get medicine details for caretakers,list all medicines that are doesnt expired
@api_view(['GET'])
def CaretakerMedicineView(request):
    data = {}
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        date=request.GET.get('date')
        data = MedModel.objects.filter(user_id=user_id)
        if not data:
            return Response('User not found',status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineSerializer(data,many=True)
        data=serializer.data
        
        dates=datetime.strptime(date, '%Y-%m-%d')
        filterdData = []
        for i in data:
            currentDate = datetime.strptime(i['endDate'][:10],'%Y-%m-%d')
            if currentDate >= dates:
                filterdData.append(i)
        if not filterdData:
            return Response('data not found',status=status.HTTP_404_NOT_FOUND)
            
    return Response(filterdData)
    
class UserPostDeleteView(GenericAPIView):
    queryset=MedModel.objects.all()
    serializer_class=MedicineSerializer
    
    def get(self,request,*args,**kwags):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)
    
    def delete(self,request,*args,**kwags):
        instance=self.get_object()
        instance.delete()
        return Response('Delted Successfully',status=status.HTTP_200_OK)

# class CaretakerHistoryView(generics.ListAPIView):
#     queryset = MedModel.objects.all()
#     serializer_class = MedicineSerializer

@api_view(['GET'])
def HistoryView(request):
    data = {}
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        date=request.GET.get('date')
        data = MedModel.objects.filter(user_id=user_id)
        if not data:
            return Response('User not found',status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineSerializer(data,many=True)
        data=serializer.data
            
    return Response(serializer.data)  
    
#get patients info,those who are listed medicines for today
@api_view(['GET',])
def history_view(request):
    data = {}
    if request.method == 'GET':
        date=request.GET.get('date')
        data=MedModel.objects.all()
        serializer = MedicineSerializer(data,many=True)
        data=serializer.data
        dates=datetime.strptime(date, '%Y-%m-%d')
        filterdData = []
        for i in data:
            currentDate = datetime.strptime(i['startDate'][:10],'%Y-%m-%d')
            if currentDate == dates:
                filterdData.append(i)
        if not filterdData:
            return Response('data not found',status=status.HTTP_404_NOT_FOUND)
        userid = []
        for i in filterdData:
            userid.append(i['user_id'])
        users=[]
        for i in userid:
            data=User.objects.filter(id=i)    
            serializer = Userserializer(data,many=True)        
            data=serializer.data
            #check for unique before appending
              
            users.append(data)

    return Response(users)