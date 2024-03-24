import requests 
api_key="e6629a0dd1d93239d79f71cbb67b7bfe"
user_input=input("Enter City ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == 404:
    print("City not found")
else:
    data = weather_data.json()
    weather_description = data['weather'][0]['description']
    temperature = int(data['main']['temp'])
    print(f"The weather in {user_input} is: {weather_description.capitalize()}")
    print(f"The temperature in {user_input} is: {temperature}ºF")
