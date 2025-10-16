from django.db import models

class prodect(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.IntegerField()
    idP=models.IntegerField()
    img=models.ImageField(upload_to="makeup/images",default="")


class clint(models.Model):
    name=models.CharField(max_length=200)
    idC=models.IntegerField()
    pas=models.CharField(max_length=200)

class order(models.Model):    
    idO=models.IntegerField()
    amount=models.IntegerField()
    idC=models.IntegerField()
    idP=models.IntegerField()

