from openwepy import *

api_key = openweather("API_KEY").api_key


coordinate = geocoding("Istanbul", api_key)

response = coordinate.make_response()
response_json = coordinate.get_response_json(response)

print(coordinate.get_lat_and_lon(response_json))
print(coordinate.get_country(response_json))


weather = current_weather(coordinate.get_lat(response_json), coordinate.get_lon(response_json), api_key)

weather_response = weather.make_response()
weather_response_json = weather.get_response_json(weather_response)

print(weather_response_json)

print(weather.get_weather(weather_response_json, weather.weather_main))
print(weather.get_weather(weather_response_json, weather.weather_description))

fahrenheit_temprature = weather.get_temprature(weather_response_json, weather.temprature_kelvin)
print(temprature.kelvin_to_celcius(fahrenheit_temprature))