import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/get-weather')
def get_weather():
    return render_template(
        'weather.html',
        location='Downers Grove',
        temp='60',
        month='April',
        description='rain')

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
