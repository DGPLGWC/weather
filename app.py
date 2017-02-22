import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Girls Who Code!'

@app.route('/hello/<string:name>')
def hello(name):
    return render_template(
        'helloname.html', name=name)

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
