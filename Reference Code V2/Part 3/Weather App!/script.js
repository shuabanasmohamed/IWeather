const weatherData = {
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"}
};

function getWeather() {
    const city = document.getElementById('city-input').value.trim();
    const weatherInfo = document.getElementById('weather-info');
    const errorMessage = document.getElementById('error-message');

    if (weatherData[city]) {
        const data = weatherData[city];
        document.getElementById('city-name').textContent = `City: ${city}`;
        document.getElementById('temperature').textContent = `Temperature: ${data.temperature}`;
        document.getElementById('conditions').textContent = `Conditions: ${data.conditions}`;
        document.getElementById('wind-speed').textContent = `Wind Speed: ${data.wind_speed}`;
        document.getElementById('humidity').textContent = `Humidity: ${data.humidity}`;

        weatherInfo.style.display = 'block';
        errorMessage.textContent = '';
    } else {
        weatherInfo.style.display = 'none';
        errorMessage.textContent = `Sorry, weather data for ${city} is not available.`;
    }
}
