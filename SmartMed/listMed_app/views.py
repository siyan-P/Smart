from rest_framework.response import Response
from listMed_app.serializers import MedicineSerializer
from rest_framework import generics
from listMed_app.models import MedModel
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework import status
# Create your views here.
class MedicineView(generics.CreateAPIView):
   queryset = MedModel.objects.all()
   serializer_class = MedicineSerializer
   

#from .models import Post
#from .serializers import PostSerializer

class UserPostListView(ListAPIView):
    serializer_class = MedicineSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return MedModel.objects.filter(user_id=user_id)
    
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
    
    

