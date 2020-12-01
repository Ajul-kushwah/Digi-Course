from django.shortcuts import render,redirect
from shop.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class SignupView(View):
    def get(self,request):
        return render(request, 'signup.html',{'active':True})

    def post(self,request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            hashPassword = make_password(password=password)
            user = User(name=name, email=email, phone=phone, password=hashPassword)
            user.save()
            return redirect('login')
        except:
            return render(request, 'signup.html',{'error':'Email already registered'})