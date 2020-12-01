from django.db import models
from shop.models import Products
from shop.models import User
# Create your models here.

class Payment(models.Model):
    product = models.ForeignKey(Products,null=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)

    payment_request_id = models.CharField(max_length=200,null=False,unique=True)
    payment_id = models.CharField(max_length=200,null=True,unique=True)
    payment_status = models.CharField(max_length=200,default='Failed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
