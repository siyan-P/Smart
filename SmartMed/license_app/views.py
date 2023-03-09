from rest_framework.decorators import api_view
from rest_framework.response import Response
from license_app.serializers import LicenseSerializer
from django.http import HttpResponse
# Create your views here.

@api_view(['POST',])
def registration_view(request):
    #data = {}
    if request.method == 'POST':
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #data['res']='Account Created successful!'
            return HttpResponse(status=200)
        
        else:
            return Response(serializer.errors)