import requests
import json
from download_products.settings import EMAIL_SERVICE_ENDPOINT, \
    EMAIL_SENDER_NAME, \
    EMAIL_SENDER_EMAIL, \
    EMAIL_API_KEY


def sendEmail(name, email, subject, htmlContent):
    # payload = {
    #     "sender": {
    #         "name": EMAIL_SENDER_NAME,
    #         "email": EMAIL_SENDER_EMAIL
    #     },
    #     "to": [
    #         {
    #             "email": email,
    #             'name': name
    #
    #         }
    #     ],
    #     'replyTo': {
    #         "email": EMAIL_SENDER_EMAIL,
    #         "name": EMAIL_SENDER_NAME
    #     },
    #     "htmlContent": htmlContent,
    #     'subject': subject
    # }
    #
    # headers = {
    #     'accept': "application/json",
    #     'content-type': "application/json",
    #     'api-key': EMAIL_API_KEY
    #     }
    #
    # response = requests.request("POST", EMAIL_SERVICE_ENDPOINT,
    #                                     data=json.dumps(payload),
    #                                     headers=headers)

    return requests.post(
        "",#api link
        auth=("api", ""),#api key
        data={"from": "",
              "to": [email],#["abcd@gmail.com"],#email
              "subject": subject,
              "html": htmlContent})


# result = sendEmail('','','testing email','<h2> hello ajul bhai </h2>')
# print(result.status_code)
