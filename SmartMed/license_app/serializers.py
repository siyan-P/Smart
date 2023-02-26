from rest_framework import serializers
from license_app.models import LicenceId

class LicenseSerializer(serializers.ModelSerializer):
    model = LicenceId
    fields = "__all__"
    
    def save(self):
        
        if LicenceId.objects.filter(regno=self.validated_data['regno']).exists():
            raise serializers.ValidationError({'error':'LicenceId already exists or invalid!'})
      
        account = LicenceId(regno=self.validated_data['regno'])
        account.save()
        return account