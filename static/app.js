function getWeather() {
    const city = document.getElementById('city').value;
    const weatherInfo = document.getElementById('weather-info');

    if (!city) {
        weatherInfo.textContent = "Please enter a city name.";
        return;
    }

    // Send city name to Flask backend via fetch API
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                weatherInfo.textContent = data.error;
                weatherInfo.className = "error";
            } else {
                weatherInfo.innerHTML = `
                    <p><strong>Weather in ${data.name}</strong></p>
                    <p>Temperature: ${data.temp}°C</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Description: ${data.description}</p>
                `;
                weatherInfo.className = "success";
            }
        })
        .catch(error => {
            weatherInfo.textContent = "Error fetching weather data.";
            weatherInfo.className = "error";
        });
}
