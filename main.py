import requests

API_KEY = ""
while True:
    CITY = input("Enter city name: ").strip()

    if CITY in ("exit", "quit"):
        print("Exiting the program.")
        break

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

            # providing suggestions based on weather conditions
            if "rain" in weather_desc.lower():
                print("💧 Take an umbrella!")
            if temp > 30:
                print("🔥 Stay hydrated!")
            if temp < 5:
                print("❄️ Wear warm clothes!")

            # asking user if they want to continue
            if input("Do you want to continue? (yes/no): ").lower() == 'yes':
                continue
            else:
                print("Exiting the program.")
                break

        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)








