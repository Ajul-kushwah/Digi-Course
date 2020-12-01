from django.shortcuts import render,HttpResponse,redirect
from shop.models import Products,ProductImage,User

from django.contrib import messages
from django.contrib.auth.hashers import \
    make_password,check_password


def index(request):
    products =Products.objects.filter(active=True)[:4]
    context = {'products':products}
    return render(request,'index.html',context)

def all_products(request):
    products = Products.objects.filter(active=True)
    context = {'products':products}
    return render(request,'all_products.html',context)

def check_email(request):
    user = User.object.get(email = request.POST.get('email'))
    try:
        user = User.objects.get(email=request.GET.get('email'))
        return HttpResponse('true')
    except:
        return HttpResponse('false')

def update_user(request):
    if request.method == 'POST':
        u = request.session.get('user')
        user = User.objects.get(id=u.get('id'))

        name = request.POST['fullName']
        email = request.POST['email']
        city = request.POST['cityName']
        phone = request.POST['phone']
        gender = request.POST['gender']

        user.name = name
        user.email = email
        user.city = city
        user.phone = phone
        user.gender = gender

        user.save()
        messages.success(request,
                         "Profile update Successfully",
                         extra_tags='success')

        return redirect('profile')
    else:
        return redirect('profile')

def change_password(request):
    if request.method == 'POST':
        u = request.session.get('user')
        user = User.objects.get(id=u.get('id'))

        cpassword = request.POST['current_password']
        npassword = request.POST['new_password']

        if check_password(cpassword,encoded=user.password):
            user.password = make_password(npassword)
            user.save()
            messages.success(request,"Change Password Successfully",extra_tags='success')
            return redirect('profile')

        else:
            messages.error(request,"password not match",extra_tags='warning')
        # print(msg)
        return redirect('profile')
    else:
        return redirect('profile')



def logout(request):
    request.session.clear()
    return redirect('index')
