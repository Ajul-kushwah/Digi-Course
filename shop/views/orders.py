from django.shortcuts import render,HttpResponse,redirect
from shop.models import Products, ProductImage, User, Payment
from django.db.models import Q

def my_orders(request):
    user_id = request.session['user'].get('id')
    user = User(id=user_id)
    payment = Payment.objects.filter(~Q(payment_status='Failed') ,user=user)
    return render(request,'orders.html',{'orders':payment,'active':True})

