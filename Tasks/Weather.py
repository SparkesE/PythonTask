weatherData = {
    "London": {
        "temperature": "15°C",
        "conditions": "Cloudy",
        "wind_speed": "5 km/h",
        "humidity": "80%"
    },
    "New York": {
        "temperature": "20°C",
        "conditions": "Sunny",
        "wind_speed": "10 km/h",
        "humidity": "50%"
    },
    "Tokyo": {
        "temperature": "18°C",
        "conditions": "Rainy",
        "wind_speed": "7 km/h",
        "humidity": "90%"
    },
    "Sydney": {
        "temperature": "22°C",
        "conditions": "Windy",
        "wind_speed": "15 km/h",
        "humidity": "60%"
    },
    "Paris": {
        "temperature": "17°C",
        "conditions": "Foggy",
        "wind_speed": "3 km/h",
        "humidity": "85%"
    }
}

def displayWeather(city):
    cityData = weatherData[city]
    print(f"\nWeather forecast for {city}:")
    print(f"Temperature: {cityData['temperature']}")
    print(f"Conditions: {cityData['conditions']}")
    print(f"Wind Speed: {cityData['wind_speed']}")
    print(f"Humidity: {cityData['humidity']}")

def getForecast():
    print("Welcome to the Weather Forecast Application!")
    
    while True:
        # Ask the user for the city name
        city = input("\nEnter the city name for the weather forecast (e.g., London, New York, Tokyo, Sydney, Paris): ").title()
        
        # Check if the city is in the hardcoded data
        if city in weatherData:
            displayWeather(city)
            break
        else:
            print(f"Sorry, we don't have data for {city}. Please try again.")
    
    # Thank the user for using the application
    print("\nThank you for using the Weather Forecast Application!")

# Call the main function to start the program
getForecast()