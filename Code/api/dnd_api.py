import requests

class DndApi():
    def __init__(self):
        self._url_base = "https://www.dnd5eapi.co/api/"

    def dnd_request(self, url_extension):
        full_url = self._url_base + url_extension
        new_request = requests.get(full_url)
        return new_request.text