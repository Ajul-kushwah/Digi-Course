from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from shop.models import User
from django.views import View
from shop.utils.email_sender import sendEmail
from django.contrib.auth.hashers import make_password,check_password

class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'reset_password.html',{'step1':True})

    def post(self, request):
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None
        if len(password) >= 6:
            if password == repassword:
                email = request.session.get('reset-password-email')
                user = User.objects.get(email = email)
                user.password = make_password(password)
                user.save()
                request.session.clear()
                sendEmailAfterChangePassword(user)
                return render(request, 'login.html', {'error': 'Password Reset successfully'})

            else:
                error = 'Password must be same'
                return render(request, 'reset_password.html', {'step3': True,'error':error})

        else:
            error = 'password must be more than 6 character'
            return render(request, 'reset_password.html', {'step3': True, 'error': error})

def sendEmailAfterChangePassword(user):
    html = f'''
        <p>Hello <b>{user.name}</b> Your Password has been reset Successfully.</p>
        <p>Please login again</p> <a href="http://localhost:8000/login">login</a>
    '''
    sendEmail(name=user.name,
              email=user.email,
              subject='Password Reset',
              htmlContent=html)

def verifyResetPasswordCode(request):
    code = request.POST.get('verify-code')
    session_code = request.session['reset-password-verification-code']
    request.session['reset-password-email']
    print(session_code)
    print(code)

    if code == str(session_code):
        return render(request, 'reset_password.html', {'step3': True})
    else:
        return render(request, 'reset_password.html', {'step2': True,'error':'invalid otp'})



import math
import random

class PasswordResetVerification(View):
    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if user:
            otp = math.floor(random.random() * 1000000)
            html=f'''
                <p> Your Password Reset Verification Code is <b>{otp}</b> .</p>
            '''
            sendEmail(name='Dear User',
                      email=email,
                      subject='Reset Password Verification Code',
                      htmlContent=html)

            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
        else:
            return render(request, 'reset_password.html',{'step1':True,'error':'Email not registered'})

        return render(request, 'reset_password.html', {'step2': True})
