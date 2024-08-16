# Hardcoded weather data
weather_data = {
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"}
}

def welcome_message():
    print("Welcome to the Python Weather App!")

def get_city_input():
    city = input("Enter the city name for the weather forecast: ").strip()
    return city

def display_weather_data(city):
    data = weather_data.get(city)
    if data:
        print(f"\nWeather forecast for {city}:")
        print(f"Temperature: {data['temperature']}")
        print(f"Conditions: {data['conditions']}")
        print(f"Wind Speed: {data['wind_speed']}")
        print(f"Humidity: {data['humidity']}")
    else:
        print(f"Sorry, weather data for {city} is not available.")
        return False
    return True

def thank_you_message():
    print("Thank you for using the weather forecast application!")

def main():
    welcome_message()
    while True:
        city = get_city_input()
        if display_weather_data(city):
            break
        else:
            print("Please enter a valid city name from the available list.")
            print("Available cities:", ", ".join(weather_data.keys()))
    thank_you_message()

if __name__ == "__main__":
    main()
