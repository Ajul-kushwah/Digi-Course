from instamojo_wrapper import Instamojo
from download_products.settings import PAYMENT_API_KEY,PAYMENT_API_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')


# Create a new Payment Request
response = api.payment_request_create(
    amount='10',
    purpose='Testing ..',
    send_email=True,
    email="ajulkushwah786@gmail.com",
    redirect_url="http://www.feelfreetocode.com"
    )

print(response)
# print the long URL of the payment request.
print(response['payment_request']['longurl'])
# print the unique ID(or payment request ID)
print(response['payment_request']['id'])
