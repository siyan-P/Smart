from django.db import models
#from django.contrib.auth.models import User
from patientsapp.models import patientsModel
# Create your models here.
class MedModel(models.Model):
    #user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='MedModel')#(User,on_delete=models.CASCADE,related_name="MedicineModel")
    id = models.AutoField(primary_key=True)
    medName = models.CharField(max_length=50)
    description = models.CharField(max_length=50,blank=True,null=True)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()
    beforeFood = models.CharField(max_length=50,blank=True,null=True)
    medicineTime = models.CharField(max_length=50,blank=True,null=True)
    medMorning = models.BooleanField()
    medNoon = models.BooleanField()
    medEvening = models.BooleanField()
    p_id = models.ForeignKey(patientsModel,on_delete=models.CASCADE,related_name='MedModel')
    doc_name = models.CharField(max_length=25,null=True,blank=True)
    doc_id = models.IntegerField(null=True,blank=True)
    
    
    def _str_(self):
        return self.id