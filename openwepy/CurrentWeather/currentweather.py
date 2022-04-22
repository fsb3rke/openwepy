import requests

class current_weather:
    def __init__(self, lat, lon, api_key: str):
        self.__lat = lat
        self.__lon = lon
        self.__api_key = api_key

    def make_response(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={str(self.__lat)}&lon={str(self.__lon)}&appid={self.__api_key}")
        return response

    def get_response_json(self, response: requests.Response):
        return response.json()

    # weather keys
    @property
    def weather_id(self):
        return "id"

    @property
    def weather_main(self):
        return "main"

    @property
    def weather_description(self):
        return "description"

    def get_weather(self, response_json: dict, key: str):
        weather_dict = response_json["weather"][0]
        return weather_dict[key]


    # temprature keys
    @property
    def temprature_kelvin(self):
        return "temp"

    @property
    def temprature_feels_like(self):
        return "feels_like"

    @property
    def minumum_temprature_kelvin(self):
        return "temp_min"

    @property
    def maximum_temprature_kelvin(self):
        return "temp_max"

    def get_temprature(self, response_json: dict, key: str):
        temprature_dict = response_json["main"]
        return temprature_dict[key]