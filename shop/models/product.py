from django.db import models
import datetime
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    sub_description = models.TextField( default="")
    description = models.TextField()
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='files',null=True,blank=True,default=None)
    thumbnail = models.ImageField(upload_to='thumbnail',null=True)
    link = models.CharField(max_length=100 ,null=True, blank=True)
    fileSize = models.CharField(max_length=100 ,null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',blank=True)