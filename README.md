# openwepy

openwepy is a Python library for use open wheather api.

## Get Json Data's

### import library
```python
import openwepy
```

### set your api key
``` python
# first you must have a api key.
api_key = openweather("api_key").api_key # or set a api key string
```

### get coordinates
``` python
# get coordinates
coordinate = geocoding("city_name", "api_key")
# make a response
response = coordinate.make_response()
# get response json
response_json = coordinate.get_response_json(response) # or you can use "response.json()"
```

### get weather stats
``` python
# get weather stats
weather = current_weather("lat", "lon", "api_key")
# make a response
weather_response = weather.make_response()
# get response json
weather_response_json = weather.get_response_json(weather_response) # or you can use "weather_response.json()"
```

## Methods
### Gecoding

```
make_response()
```
```
get_response_json(response)
```
```
get_lat(response_json)
```
```
get_lon(response_json)
```
```
get_lat_and_lon(response_json)
```
```
get_country(response_json)
```

### Current Weather

```
make_response()
```
```
get_response_json(response)
```
#### Weather
```
get_weather(response_json, key)
```
```
weather_id
```
```
weather_main
```
```
weather_description
```

#### Temprature
```
get_temprature(response_json, key)
```
```
temprature_kelvin
```
```
temprature_feels_like
```
```
minumum_temprature_kelvin
```
```
maximum_temprature_kelvin
```

#### Wind
```
get_wind(response_json, key)
```
```
wind_speed
```
```
wind_degree
```

# Extra's
## Temprature Converter Library
### Methods
```
celcius_to_fahrenheit(celcius)
```
```
fahrenheit_to_celcius(fahrenheit)
```
```
kelvin_to_fahrenheit(kelvin)
```
```
fahrenheit_to_kelvin(fahrenheit)
```
```
kelvin_to_celcius(kelvin)
```
```
celcius_to_kelvin(celcius)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
openwepy is distributed under MIT license.

for more information:
[MIT](https://choosealicense.com/licenses/mit/)
