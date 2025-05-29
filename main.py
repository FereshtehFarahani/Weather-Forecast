import requests

API_KEY = ""
while True:
    CITY = input("Enter city name: ")
    res = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    try:
        response = requests.get(res)
        if response.status_code == 200:
            data = response.json()  # parse JSON response
            #print(data)
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    if 'data' not in locals():  
        print("Failed to retrieve data. Please check the city name and try again.")
        continue
    
    # extracting needed data 
    city = data['name']
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather_desc}")
    print(f"Humidity: {humidity}%")

    if input("Do you want to continue? (yes/no): ").lower() == 'yes':
        continue
    else:
        print("Exiting the program.")
        break





