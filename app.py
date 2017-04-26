import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/get-weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    print 'Hello ' + city
    return render_template(
        'weather.html',
        location=city,
        temp='73',
        month='April',
        description='overcast')

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
