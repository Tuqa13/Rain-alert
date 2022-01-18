import requests
from twilio.rest import Client


account_sid = "ACf832560790170b91445f261a4e02f057"
auth_token = "6f1b173f71a1af41e44cf7ecbeb8d2dc"

parameters = {
    "lat": 31.945368 ,
    "lon": 35.928371,
    "exclude": "current,minutely,daily",
    "appid": "8cf0d29e8a80d55e18a11b893d131e96",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"][:12]
for hour_data in data:
    if hour_data["weather"][0]["id"] > 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It will rain today!\nMake sure to bring your Umbrella ☂️☂️",
            from_="+12244790631",
            to="+962786790258"
        )

        print(message.status)
        break


# import requests
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
#
# account_sid = "ACf832560790170b91445f261a4e02f057"
# auth_token = "6f1b173f71a1af41e44cf7ecbeb8d2dc"
#
# parameters = {
#     "lat": 31.945368 ,
#     "lon": 35.928371,
#     "exclude": "current,minutely,daily",
#     "appid": "8cf0d29e8a80d55e18a11b893d131e96",
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# data = response.json()["hourly"][:12]
# for hour_data in data:
#     if hour_data["weather"][0]["id"] > 700:
#         proxy_client = TwilioHttpClient()
#         proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#         client = Client(account_sid, auth_token, http_client=proxy_client)
#         message1 = client.messages.create(
#             body="It Will Rain Today!\nMake Sure to Bring your Umbrella ☂️☂️",
#             from_="+12244790631",
#             to="+962786790258"
#         )
#
#         message2 = client.messages.create(
#             body="It Will Rain Today!\nMake Sure to Bring your Umbrella ☂️☂️",
#             from_="+12244790631",
#             to="+962790296658"
#         )
#
#         print(message1.status)
#         print(message2.status)
#         break
