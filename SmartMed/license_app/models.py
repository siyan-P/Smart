from django.db import models

# Create your models here.
class LicenceId(models.Model):
    id = models.IntegerField(auto_created=True)
    regno = models.CharField(max_length=50,primary_key=True)
    
    # def __int__(self):
    #     return self.regno
    
    
