from openwepy import *
from tabulate import tabulate

api_key = openweather("api_key").api_key

city = "Istanbul"

coordinate = geocoding(city, api_key)

response = coordinate.make_response()
response_json = coordinate.get_response_json(response)

weather = current_weather(coordinate.get_lat(response_json), coordinate.get_lon(response_json), api_key)

weather_response = weather.make_response()
weather_response_json = weather.get_response_json(weather_response)

kelvin_temprature = weather.get_temprature(weather_response_json, weather.temprature_kelvin)
celcius_temprature = temprature.kelvin_to_celcius(kelvin_temprature)

weather_main = weather.get_weather(weather_response_json, weather.weather_main)

table = [["City", "Weather", "Temprature", "Wind"], [city, weather.get_weather(weather_response_json, weather.weather_main), celcius_temprature, weather.get_wind(weather_response_json, weather.wind_speed)]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))