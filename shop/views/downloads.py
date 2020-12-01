from django.shortcuts import render, HttpResponse, redirect
from shop.models import Products, Payment, User


def downloadFreeProduct(request, product_id):
    # try:
    product = Products.objects.get(id=product_id)
    if product.discount == 100:
        file = None
        file = product.file.url
        if file:
            return redirect(product.file.url)
        else:
            return redirect(product.link)
    else:
        return redirect('index')


# except:
#     return redirect('index')


def downloadPaidProduct(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
        print(product)
        session_user = request.session['user']
        user = User(id=session_user.get('id'))
        payment = Payment.objects.filter(user=user, product=product)
        print(payment)

        if len(payment) > 0:
            file = product.file
            if file:
                return redirect(product.file.url)
            else:
                return redirect(product.link)
        else:
            return redirect('index')
    except:
        return redirect('index')
