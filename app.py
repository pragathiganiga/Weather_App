from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API key (replace with your own)
API_KEY = "e0a58ede38563acdfe4c54df265e5322"

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get the city from the URL parameter
    if city:
        # Construct the API URL dynamically using the city and API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q=London&appid=e0a58ede38563acdfe4c54df265e5322&units=metric'
        
        # Make the request to the OpenWeatherMap API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:  # Check if the response was successful
            # Extract weather information
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Return the weather data in JSON format
            return jsonify({
                'status': 'success',
                'weather': weather,
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed
            })
        else:
            # If the city is not found or there is another error
            return jsonify({'status': 'error', 'message': 'City not found or invalid'})
    return jsonify({'status': 'error', 'message': 'City parameter missing'})

if __name__ == '__main__':
    app.run(debug=True)
