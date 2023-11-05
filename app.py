from flask import Flask, render_template, request
import json
from weather import get_weather

import urllib.request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather_req():
    if request.method == 'POST':
        city = request.form['city'].strip()
        state = request.form['state'].strip()
        country = request.form['country'].strip()
        if city != "" and state != "" and country != "":
            data = get_weather(city, state, country)
        else:
            data = None
        print(data)
    else:
        data = None
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
