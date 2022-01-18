import requests
from twilio.rest import Client


account_sid = "ACf83256079017*********e02f057"
auth_token = "6f1b173f71a*********beb8d2dc"

parameters = {
    "lat": 31.945368 , // Amman location
    "lon": 35.928371,
    "exclude": "current,minutely,daily",
    "appid": "8cf0d29e8a80d******3d131e96",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"][:12] // To check all the hours during the day
for hour_data in data:
    if hour_data["weather"][0]["id"] > 700: // if the id > 700, then it will rain
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It will rain today!\nMake sure to bring your Umbrella ☂️☂️",
            from_="+122*****31", 
            to="+9627*****258"
        )

        print(message.status)
        break

