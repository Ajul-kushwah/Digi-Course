from django.shortcuts import render, redirect, HttpResponse
from shop.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from shop.utils.email_sender import sendEmail
import math
import random


class sendOtpView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        otp = math.floor(random.random() * 1000000)
        print(name, email)
        html = f'''
                <h4>Hello {name},</h4>
                <br>
                <p>Your Verification Code is <b>{otp}</b> </p>
                <br>
                <p>If you did not request for otp then you can ignore this email.<p>
                Our website is <a href="www.ajul.com">www.ajul.com</a>
        '''
        # email sending
        if name and email:
            response = sendEmail(name=name, email=email, subject="Verification Code for create account", htmlContent=html)

            try:
                if response.status_code:
                    request.session['verification-code'] = otp
                    return HttpResponse("{'message':'success'}", status=200)
                else:
                    return HttpResponse(status=400)
            except:
                return HttpResponse(status=400)


class verifyCodeView(View):
    def post(self,request):
        code = request.POST.get('code')
        otp = request.session.get('verification-code')
        print(code, '  ', otp)
        if str(otp) == code:
            return HttpResponse("{'message':'success'}", status=200)
        else:
            return HttpResponse(status=400)
