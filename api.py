import requests

latitudde = 40.7128
longitude = -74.0060

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitudde}&longitude={longitude}&current_weather=true"


response = requests.get(url)
data=response.json()

print(data)


type(data)
data.keys()

data["current_weather"]["temperature"]
