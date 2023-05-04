from django.db import models
from listMed_app.models import MedModel
from patientsapp.models import patientsModel
# Create your models here.
class medAnalytics(models.Model):
    id = models.AutoField(primary_key=True)
    m_id = models.ForeignKey(MedModel,on_delete=models.CASCADE,related_name='medAnalytics')
    p_id = models.ForeignKey(patientsModel,on_delete=models.CASCADE,related_name='medAnalytics')
    medName = models.ForeignKey(MedModel,on_delete=models.CASCADE,related_name='MedModel')
    Date = models.DateTimeField()
    morningTaken = models.CharField(max_length=25,blank=True,null=True)
    noonTaken = models.CharField(max_length=25,blank=True,null=True)
    eveningTaken = models.CharField(max_length=25,blank=True,null=True)