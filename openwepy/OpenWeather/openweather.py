class openweather:
    def __init__(self, api_key):
        self.__api_key = api_key

    @property
    def api_key(self):
        return self.__api_key