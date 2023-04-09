from rest_framework.decorators import api_view
from rest_framework.response import Response
from license_app.serializers import LicenseSerializer
from django.http import HttpResponse
from django.shortcuts import render
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
        
@api_view(['GET',])
def privacy_policy(request):
        if request.method == 'GET':
            return Response('This is the privacy policy for our health app.We take the privacy of our users very seriously, and we are committed to protecting it. Information we collect:- We collect basic information such as name, email, and phone number to create user accounts.- We collect health information such as medical history, medications, and allergies to provide personalized health recommendations.Security:We use industry-standard security measures to protect user information.We regularly review and update our security measures to ensure the safety of user information.If you have any questions or concerns about our privacy policy, please contact us at smartmeds@gmail.com')
       
    

    
