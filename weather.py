import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class Weather:
    main: str
    description: str
    icon: str
    temp: int
    feels_like: int
    name: str
    humidity: int
    wind: int
    pressure: int


def get_coordinates(city_name=None, state_code=None, country_code=None, API_key=None):
    response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    lat, lon = response[0].get('lat'), response[0].get('lon')
    print(response)
    return lat, lon


def get_current_weather(lat=None, lon=None, API_key=None):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = Weather(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temp=int(response.get('main').get('temp')),
        feels_like=int(response.get('main').get('feels_like')),
        name=response.get('name'),
        humidity=response.get('main').get('humidity'),
        wind=response.get('wind').get('speed'),
        pressure=response.get('main').get('pressure')
    )
    print(response)
    return data


def get_weather(city, state, country):
    lat, lon = get_coordinates(city, state, country, api_key)
    return get_current_weather(lat, lon, api_key)

