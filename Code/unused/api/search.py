import requests
import json


class Search():
    def __init__(self, url_extension):
        self._url_base = "https://www.dnd5eapi.co"
        self._url_extension = url_extension
        self._full_url = self._url_base + self._url_extension
        self._json = json.loads(requests.get(self._full_url).text)

    def reset(self, url_extension):
        self.__init__(url_extension)
    
    def get_json(self):
        return self._json

    def get(self, field):
        return self._json[field]



class SearchList(Search):
    def __init__(self, url_extension):
        super().__init__(url_extension)
        self._count = self._json["count"]
        self._original_results = self._json["results"]
        self._results = self._format_results_dictionary()

    def _format_results_dictionary(self):
        new_results = {}
        for result in self._original_results:
            new_results[(result["index"])] = result
        return new_results

    def get_results(self):
        return self._results


class SearchSpecific(Search):
    pass


# def main():
#     monsters = SearchList("monsters")
#     print (monsters._count)
#     print (monsters._results)

#     monsters.reset("classes")
#     print (monsters._count)
#     print (monsters._results)

# main()