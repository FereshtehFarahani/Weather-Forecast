import requests
import csv
import os
from datetime import datetime

def fetch_data():
    API_KEY = ""
    cities = input("Enter city names (comma-separated): ").split(',')
    for CITY in cities:
        CITY = CITY.strip()   
        if CITY in ("exit", "quit"):
            print("Exiting the program.")
            sys.exit()

        res = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(res)
            if response.status_code == 200:
                data = response.json()  # parse JSON response
                #print(data)
                # extracting needed data 
                city = data['name']
                weather_desc = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                print(f"City: {city}")
                print(f"Temperature: {temp}°C")
                print(f"Weather: {weather_desc}")
                print(f"Humidity: {humidity}%")

                # save data in csv 
                captured_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_exists = os.path.isfile('data/weather_log.csv')
                with open('data/weather_log.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(["timestamp", "city", "temperature", "weather_description", "humidity"])
                    writer.writerow([captured_time, city, temp, weather_desc, humidity])

                # providing suggestions based on weather conditions
                if "rain" in weather_desc.lower():
                    print("💧 Take an umbrella!")
                if temp > 30:
                    print("🔥 Stay hydrated!")
                if temp < 5:
                    print("❄️ Wear warm clothes!")                    
            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            









