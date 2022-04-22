import requests

class geocoding:
    def __init__(self, city_name: str, api_key: str, limit=5):
        self.__city_name = city_name
        self.__limit = limit
        self.__api_key = api_key

    def make_response(self):
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.__city_name}&limit={str(self.__limit)}&appid={self.__api_key}")
        return response

    def get_response_json(self, response: requests.Response):
        return response.json()

    def get_lat(self, response_json: list):
        list_first_index = response_json[0]
        lat = list_first_index["lat"]
        return lat

    def get_lon(self, response_json: list):
        list_first_index = response_json[0]
        lon = list_first_index["lon"]
        return lon

    def get_lat_and_lon(self, response_json: list):
        list_first_index = response_json[0]
        lat = list_first_index["lat"]
        lon = list_first_index["lon"]
        return [lat, lon]

    def get_country(self, response_json: list):
        list_first_index = response_json[0]
        country = list_first_index["country"]
        return country