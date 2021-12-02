from api.search import SearchList

DICE_OPTIONS = [2,4,6,8,10,12,20,100]
ABILITY_OPTIONS = SearchList("/api/ability-scores/")
ABILITY_SCORES = [15,14,13,12,10,8]

print (ABILITY_OPTIONS)