from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MedModel(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='MedModel')#(User,on_delete=models.CASCADE,related_name="MedicineModel")
    id = models.AutoField(primary_key=True,)
    medName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()
    beforeFood = models.BooleanField(default=False)
    medMorning = models.BooleanField(default=False)
    medNoon = models.BooleanField(default=False)
    medEvening = models.BooleanField(default=False)
    
    
    def _str_(self):
        return self.id