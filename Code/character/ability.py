class Ability():
    def __init__(self, score, search_object):
        self.set_score(score)

    def set_score(self, score):
        self._score = score
        self._modifier = score // 2 - 5

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._name

    def get_modifier(self):
        return self._modifier
