from django.shortcuts import redirect,render

def login_required(get_response):

    def middleware(request,product_id=None):
        user = request.session.get('user')
        if user:
            if product_id:
                response = get_response(request,product_id)
                return response
            else:
                response = get_response(request)
                return response
        else:
            url = request.path
            print(url)
            return redirect(f'/login?return_url={url}')

    return middleware