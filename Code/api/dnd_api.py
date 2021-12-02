import requests
import json

class DndApi():
    def __init__(self):
        self._url_base = "https://www.dnd5eapi.co/api/"

    def dnd_request(self, url_extension):
        full_url = self._url_base + url_extension
        new_request = requests.get(full_url)
        return  json.loads(new_request.text)

    def dnd_return_list(self, dnd_json, field):
        desired_info = {}
        results = dnd_json["results"]
        for result in results:
            desired_info[(result[field])] = result
        return desired_info

    def dnd_return_json(self, dnd_json, field):
    desired_info = {}
    results = dnd_json["results"]
    for result in results:
        desired_info[(result[field])] = result
    return desired_info


    def dnd_request_list(self, url_extension, field):
        dnd_json = self.dnd_request(url_extension)
        return self.dnd_return_list(dnd_json, field)