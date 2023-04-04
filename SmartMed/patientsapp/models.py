from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class patientsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=25)
    p_email = models.EmailField(max_length=25,unique=True)
    p_bloodGroup = models.CharField(max_length=10)
    p_dob = models.DateField()
    c_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='patientModel')
    nfc_id = models.CharField(max_length=50,blank=True,null=True)

    def _str_(self):
        return self.p_email
