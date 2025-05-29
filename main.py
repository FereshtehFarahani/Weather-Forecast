import requests

API_KEY = ""
CITY = input("Enter city name: ")
res = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
response = requests.get(res)
if response.status_code == 200:
    data = response.json()  # parse JSON response
    #print(data)
else:
    print("Error:", response.status_code)

# extracting needed data 
city = data['name']
weather_desc = data['weather'][0]['description']
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f"City: {city}")
print(f"Temperature: {temp}°C")
print(f"Weather: {weather_desc}")
print(f"Humidity: {humidity}%")



