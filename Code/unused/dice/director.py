from dice import Dice

class Director():
    def __init__(self):
        self.dice_bag = {}
        for sides in [2,4,6,8,10,12,20,100]:
            name = "d" + str(sides)
            self.dice[name] = Dice(name, sides)

    def roll_user_dice(self):
        user_dice = input("Which dice would you like to roll? ")
        try:
            print(self.dice_bag[user_dice].roll())
        except:
            print("Please choose a valid dice option.")


    
    
def main():
    while True:
        director = Director()
        director.roll_user_dice()

main()