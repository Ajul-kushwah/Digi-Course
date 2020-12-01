from django.shortcuts import render,redirect
from shop.models import User
from django.views import View


class ProfileView(View):
    def get(self, request):
        u = request.session.get('user')
        user = User.objects.get(id=u.get('id'))

        # name = user.name
        # email = user.email
        # phone = user.phone

        return render(request, 'profile.html',{'user':user,'active':True})