from django.db import models

class Prodect(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="makeup/images",default="") 
    def __str__(self):
        return f"{self.name}"



class Clint(models.Model):
    name=models.CharField(max_length=200)
    pas=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"



class Order(models.Model):    
    clint = models.ForeignKey('Clint', on_delete=models.CASCADE, null=True, blank=True)
    prodects=models.ManyToManyField(Prodect,through='OrderedProduct')
    
    def __str__(self):
        return f"order {self.id} by {self.clint.name}"


class OrderedProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    prodect=models.ForeignKey(Prodect,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.prodect.name} ,the amount ={self.amount}"

