from django.shortcuts import render,redirect
from shop.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class LoginView(View):
    return_url = None
    def get(self, request):
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html',{'active':True})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                temp = {}
                temp['id']=user.id
                temp['email']=user.email
                request.session['user'] = temp
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'Invaild email, Password'})

        except:
            return render(request, 'login.html', {'error': 'Email already registered'})