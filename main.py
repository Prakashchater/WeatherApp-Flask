from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime


weather_api_key = "592dd33a1092d9eca5c1b173c4d88ee9"

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///weather.db'
# app.config['SECRET_KEY'] = "qwertyuioplkjhgfdsa"
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# db = SQLAlchemy(app)


# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

# db.create_all()

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form['city']
    else:
        correct = False
        
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city.title()}&units=metric&appid=592dd33a1092d9eca5c1b173c4d88ee9"
    response = requests.get(url=weather_url).json()
    weather_data = {
        'city': response['name'],
        'temperature': response['main']['temp'],
        'weather': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'min_temp': response['main']['temp_min'],
        'max_temp': response['main']['temp_max'],
        'humidity': response['main']['humidity'],
        'time': datetime.now().strftime('%H:%M')
        }
    return render_template('index.html', weather = weather_data, correct=True)


if __name__ == "__main__":
    app.run(debug=True)
