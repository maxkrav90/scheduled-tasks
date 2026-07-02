import requests
import twilio.rest
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


LAT = 43.6534817
LONG =-79.3839347
id = 10000

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()


for num in range(0,4):
    if data["list"][num]["weather"][0]["id"] < id:
        id = data["list"][num]["weather"][0]["id"]

if id < 700:
    print("Bring an umbrella")



client = twilio.rest.Client(account_sid, auth_token)

message = client.messages.create(
  from_="whatsapp:+14155238886",
  body="It's going to rain today. Remember to bring an umbrella",
  to="whatsapp:+16472620907"
)
