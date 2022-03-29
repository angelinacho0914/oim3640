import urllib.request
import json
import config


def get_current_temp(city):
    """
    Returns current temperature in Celsius in your hometown
     from api.openweathermap.org
    Notice: the temperature returned from the API is in Kelvin.
    Below is the conversion formula form Kelvin to Celsius:
    T(°C) = T(°K) - 273.15
    """
    # Can import api key that can be put in another file and not push it
    city = city.replace(' ', '%20')
    APIKEY = config.APIKEY
    country_code = 'us'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # print(response_data)
    temp = response_data.get('main')['temp']
    return temp - 273.15


def main():
    get_current_temp('wellesley')

if __name__ == '__main__':
    main()
