from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime


weather_api_key = "592dd33a1092d9eca5c1b173c4d88ee9"

app = Flask(__name__)

@app.route('/')
def home():

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=592dd33a1092d9eca5c1b173c4d88ee9"
    response = requests.get(url=weather_url).json()
    weather = {
        'city': response['name'],
        'temperature': response['main']['temp'],
        'weather': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'min_temp': response['main']['temp_min'],
        'max_temp': response['main']['temp_max'],
        'humidity': response['main']['humidity'],
        'time': datetime.now().strftime('%I:%M')
    }
    print(weather)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
