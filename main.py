import datetime as dt
import requests
from bs4 import BeautifulSoup


# -------------------------------------------------------------------------------------------------

def main():
# -------------------------------------------------------------------------------------------------
    # All functions used in program
    # function to convert Kelvin to celsius & fahrenheit
    def kelvin_to_celsius_and_fahrenheit(kelvin):
        celsius = kelvin - 273.15

        fahrenheit = (celsius * 9 / 5) + 32

        return celsius, fahrenheit

    # function to get the weather
    weather_url = 'https://weather.com/weather/today/l/34ca4f55af04e43b8206804a5247bfdbe7402506bae151bd84b87d3c55e1dddd'

    def getWeather():
        page = requests.get(weather_url)

        soup = BeautifulSoup(page.content, "html.parser")

        location = soup.find('h1', class_='CurrentConditions--location--1YWj_').text

        temperature = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text

        weather_prediction = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').text

        return location, temperature, weather_prediction

# -------------------------------------------------------------------------------------------------
    # This section is used to gather the weather report from an openweather API

    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    API_key = "1259032a7ce138f20a8dd92db5b2594f"

    current_city = "Fort Myers"

    open_url = base_url + "appid=" + API_key + "&q=" + current_city

    response = requests.get(open_url).json()

    temp_kelvin = response['main']['temp']

    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)

    humidity = response['main']['humidity']

    sky_description = response['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f'This is your daily weather report. Sunrise - {sunrise_time}, sunset - {sunset_time}')

    print(f'Current temperature in {current_city}, FL is: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F')

# -------------------------------------------------------------------------------------


    location, temperature, weather_prediction = getWeather()
    print(f'Currently, it is {sky_description} in {location} with a temperature between {temp_fahrenheit:.2f}° and {temperature}')


main()
