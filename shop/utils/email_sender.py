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
        "https://api.mailgun.net/v3/sandbox9ca2cb3e56534a23a4568458a9d3a266.mailgun.org/messages",
        auth=("api", "f6dd23f2255bb16a341a8f575d705f0c-203ef6d0-f8635cc1"),
        data={"from": "Ajul Kushwah <ajul@sandbox9ca2cb3e56534a23a4568458a9d3a266.mailgun.org>",
              "to": [email],#["ajulkushwah786@gmail.com"],
              "subject": subject,
              "html": htmlContent})


# result = sendEmail('','','testing email','<h2> hello ajul bhai </h2>')
# print(result.status_code)
