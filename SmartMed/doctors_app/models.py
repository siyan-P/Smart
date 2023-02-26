from django.db import models

# Create your models here.


class DrModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    licenseid = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    token = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username