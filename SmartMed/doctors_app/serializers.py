from rest_framework import serializers
from doctors_app.models import DrModel
from license_app.models import LicenceId
import uuid

class DrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrModel
        #fields = "__all__"
        exclude = ["id",'token']
        extra_kwargs = {'password':{'write_only':True}
                        }
        
    def save(self):
        password = self.validated_data['password']
        
        if DrModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        # if User.objects.filter(username=self.validated_data['username']).exists():
        #     raise serializers.ValidationError({'error':'email already exists'})
        if DrModel.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'username already exists'})
        #if LicenceId.objects.filter(pk=DrModel.objects.filter(regno=self.validated_data['regno'])).DoesNotExist():
        
        #no=self.validated_data['licenceid']
        regno=self.validated_data['licenseid']
        
        if LicenceId.objects.filter(regno=regno).exists():
            account = DrModel(email=self.validated_data['email'],username=self.validated_data['username'],token=str(uuid.uuid4()),licenseid=self.validated_data['licenseid'],password=self.validated_data['password'])
            #account.set_password(password)
            account.save()
            return account
        else:
            raise serializers.ValidationError({'error':'doctor does not exists'})
        
# class DrModelSerializerLogin(serializers.ModelSerializer):
#     class Meta:
#         model = DrModel
#         #fields = "__all__"
#         exclude = ["id",'token',"email",]
#         extra_kwargs = {'password':{'write_only':True}
#                         }
        
#     def save(self):
#         password = self.validated_data['password']
        
#         if DrModel.objects.filter(email=self.validated_data['email']).exists():
#             raise serializers.ValidationError({'error':'email already exists'})
        
#         # if User.objects.filter(username=self.validated_data['username']).exists():
#         #     raise serializers.ValidationError({'error':'email already exists'})
#         if DrModel.objects.filter(username=self.validated_data['username']).exists():
#             raise serializers.ValidationError({'error':'username already exists'})
#         #if LicenceId.objects.filter(pk=DrModel.objects.filter(regno=self.validated_data['regno'])).DoesNotExist():
        
#         #no=self.validated_data['licenceid']
#         regno=self.validated_data['licenseid']
        
#         if LicenceId.objects.filter(regno=regno).exists():
#             account = DrModel(email=self.validated_data['email'],username=self.validated_data['username'],token=str(uuid.uuid4()),licenseid=self.validated_data['licenseid'],password=self.validated_data['password'])
#             #account.set_password(password)
#             account.save()
#             return account
#         else:
#             raise serializers.ValidationError({'error':'doctor does not exists'})
            
        
        
        
       
        
        
        

