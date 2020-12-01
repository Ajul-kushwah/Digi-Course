from django.shortcuts import redirect,render

def cantAccessAfterLogin(get_response):

    def middleware(request):
        user = request.session.get('user')
        if user:
            # don't serve page login, signup page
            return redirect('index')
        else:
            return get_response(request)

    return middleware