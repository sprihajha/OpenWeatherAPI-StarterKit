from flask import Flask, render_template
import requests

lat = '50'
lon = '50'
appid = '*API_Key*'

def convertToFahrenheit(temp):
    float(temp)
    return int((temp - 273.15) * 1.8 + 32)

app = Flask(__name__)
@app.route('/',  methods=('GET', 'POST'))
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lat+'&appid='+appid
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    print(response_json)
    cityName = response_json['name']
    icon = response_json['weather'][0]['icon']
    temp = convertToFahrenheit(response_json['main']['temp'])
    icon_url = f'http://openweathermap.org/img/wn/{icon}@2x.png'
    return render_template("index.html", cityName=cityName, icon_url=icon_url, temp=str(temp))
