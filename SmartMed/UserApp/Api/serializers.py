from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']   
        extra_kwargs = {'password':{'write_only':True}
                        }
        
    def save(self):
        password = self.validated_data['password']
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        # if User.objects.filter(username=self.validated_data['username']).exists():
        #     raise serializers.ValidationError({'error':'email already exists'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
    

        