#! /usr/bin/env python3
import requests

from settings import WEATHER_API_HOST, WEATHER_API_KEY


def get_weather_forecast(city: str) -> str:
    api_path = '{api_host}/data/2.5/forecast?q={city},{country}&units={units}&appid={api_key}'
    country = 'usa'
    unit = 'imperial'
    temp_unit = 'fahrenheit'
    url = api_path.format(api_host=WEATHER_API_HOST, city=city, country=country, units=unit, api_key=WEATHER_API_KEY)
    temp = requests.get(url).json()['list'][0]['main']['temp']

    return 'It\'s currently {temp}° {unit} in {city}, {country}.'.format(
        temp=round(temp),
        unit=temp_unit,
        city=city.capitalize(),
        country=country.upper()
    )


if __name__ == '__main__':
    city = input('City: ').strip().lower()
    print(get_weather_forecast(city))
