from django.db import models
# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
   #customer =models.ForeignKey(Category,on_delete=models.CASCADE)
    email= models.CharField(max_length=100) 
    phone= models.IntegerField(max_length=10)
    address= models.CharField(max_length=100) 
    #description = models.TextField()
    def __str__(self):
        return self.name