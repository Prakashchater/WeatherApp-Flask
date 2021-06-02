from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime


weather_api_key = "592dd33a1092d9eca5c1b173c4d88ee9"

app = Flask(__name__)

def get_weather_data(city):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=592dd33a1092d9eca5c1b173c4d88ee9"
    response = requests.get(url=weather_url)
    return response

@app.route('/', methods=["GET","POST"])
def home():
    err_msg = ' '
    city = request.form.get('city')
    try: 
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=592dd33a1092d9eca5c1b173c4d88ee9"
        response = requests.get(url=weather_url).json()
        weather = {
        'city': response['name'],
        'temperature': response['main']['temp'],
        'weather': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'min_temp': response['main']['temp_min'],
        'max_temp': response['main']['temp_max'],
        'humidity': response['main']['humidity'],
        'time': datetime.now().strftime('%H:%M'),
        }
        return render_template('index.html', weather=weather)
    except KeyError:
        if request.method == "POST":
            city = request.form.get('city')
            if response['cod'] == 200:
                return render_template('index.html', weather=weather)
            else:
                err_msg = "Not found"
    except UnboundLocalError:
        return render_template('index.html', weather=weather)
    finally:
        return render_template('index.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
