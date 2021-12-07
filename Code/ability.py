class Ability():
    def __init__(self, score, name):
        self.set_score(score)
        # self._search_object = search_object
        self._name = name

    def set_score(self, score):
        self._score = score
        self._modifier = score // 2 - 5

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._name

    def get_modifier(self):
        return self._modifier