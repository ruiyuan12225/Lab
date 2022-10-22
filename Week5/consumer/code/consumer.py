from flask import Flask, render_template
import json
import os
import requests

app = Flask(__name__)

@app.route('/')
def show_meal():

    url = 'http://{api_host}:{api_port}'.format(api_host=os.environ.get('API_HOST'),
                                                api_port=os.environ.get('API_PORT'))
    response = requests.get(url)
    data = response.json()
    meal = data['Meal']
    price = data['Price']
    return render_template('yummy.html', meal=meal, price=price)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('CONSUMER_PORT'))