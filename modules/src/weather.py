import os

import requests

import config
from templates.text import TextTemplate

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', config.GOOGLE_MAPS_API_KEY)
OPEN_WEATHER_MAP_ACCESS_TOKEN = os.environ.get('OPEN_WEATHER_MAP_ACCESS_TOKEN', config.OPEN_WEATHER_MAP_ACCESS_TOKEN)


def process(input, entities):
    output = {}
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(
            entities['location'][0]['resolved']['values'][0]['coords']['lat']) + '&lon=' + str(
            entities['location'][0]['resolved']['values'][0]['coords']['long']) + '&units=metric&appid=' + OPEN_WEATHER_MAP_ACCESS_TOKEN
        r = requests.get(url)
        weather_data = r.json()
        output['input'] = input
        temperature_in_fahrenheit = weather_data['main']['temp'] * 1.8 + 32
        degree_sign = u'\N{DEGREE SIGN}'
        output['output'] = TextTemplate(
            'Location: ' + entities['location'][0]['resolved']['values'][0]['name'] + '\nWeather: ' +
            weather_data['weather'][0][
                'description'] + '\nTemperature: ' + str(
                weather_data['main']['temp']) + ' ' + degree_sign + 'C / ' + str(
                temperature_in_fahrenheit) + ' ' + degree_sign + 'F\n- Info provided by OpenWeatherMap').get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t get the weather info you asked for.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - tell me the weather in London'
        error_message += '\n  - weather Delhi'
        error_message += '\n  - What\'s the weather in Texas?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
