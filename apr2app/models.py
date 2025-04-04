from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    ch=[("admin","admin"),
        ("owner","owner"),
        ("consumer","consumer")]
    username=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    role=models.CharField(choices=ch,max_length=100,blank=True)
    REQUIRED_FIELDS=["role"]
    USERNAME_FIELD="email"


    def __str__(self):
        return self.email
    
class Shipment(models.Model):
    shipmentId=models.IntegerField(unique=True)
    shipmentUser=models.CharField(max_length=200)
    shipmentCategory=models.CharField(max_length=200)
    shipmentQuantity=models.IntegerField(null=False)

    def __str__(self):
        return self.shipmentId