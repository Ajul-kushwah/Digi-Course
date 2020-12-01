from django.shortcuts import render, HttpResponse, redirect
from shop.models import Products, User ,Payment
import math
from instamojo_wrapper import Instamojo
from download_products.settings import PAYMENT_API_KEY, PAYMENT_API_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')


def createPayment(request, product_id):
    user = request.session.get('user')
    email = user.get('email')
    userObj = User.objects.get(id=user.get('id'))
    user_name = userObj.name
    phone = userObj.phone

    product = Products.objects.get(id=product_id)
    amount = product.price - (product.price * product.discount / 100)

    response = api.payment_request_create(
        amount=math.floor(amount),
        purpose=f'Payment for {product.name} course',
        send_email=True,
        buyer_name=user_name,
        email=email,
        # phone=phone,
        redirect_url="http://localhost:8000/complete-payment"
    )

    print(response)
    # print the long URL of the payment request.
    # print(response['payment_request']['longurl'])


    url = response['payment_request']['longurl']

    # print the unique ID(or payment request ID)
    # print(response['payment_request']['id'])
    payment_request_id = response['payment_request']['id']
    payment = Payment(product=product,
                      user=userObj,
                      payment_request_id=payment_request_id,
                      )
    payment.save()

    return redirect(url)

def verifyPayment(request):
    user = request.session.get('user')
    userObj = User.objects.get(id=user.get('id'))

    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')

    response = api.payment_request_payment_status(
                                    payment_request_id,
                                    payment_id)

    status = response['payment_request']['payment']['status']

    if status != 'Failed':
        payment = Payment.objects.get(payment_request_id=payment_request_id)
        payment.payment_id = response['payment_request']['payment']['payment_id']
        payment.payment_status = status
        payment.save()
        # print(payment_request_id ,payment_id)
        return render(request,'download_product_after_payment.html',{'payment':payment})
    else:
        return render(request, 'payment_fail.html')
