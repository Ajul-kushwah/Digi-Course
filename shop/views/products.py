from django.shortcuts import render,redirect
from shop.models import User
from shop.models import Products,ProductImage,Payment
from django.db.models import Q

def productDetails(request,product_id):
    product = Products.objects.get(id=product_id)
    session_user = request.session['user']
    can_download = False

    if session_user:
        user_id = session_user.get('id')
        user = User(id=user_id)
        payment = Payment.objects.filter(~Q(payment_status='Failed'),product=product,user=user)
        if len(payment) !=0:
            can_download =True

    images = ProductImage.objects.filter(product=product_id)
    context={'product':product,
             'images':images,
             'can_download':can_download}
    print(images)
    return render(request,'product_details.html',context)
