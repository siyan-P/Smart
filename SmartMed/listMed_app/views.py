from rest_framework.response import Response
from listMed_app.serializers import MedicineSerializer
from rest_framework import generics
from listMed_app.models import MedModel

# Create your views here.
class MedicineView(generics.CreateAPIView):
   queryset = MedModel.objects.all()
   serializer_class = MedicineSerializer
