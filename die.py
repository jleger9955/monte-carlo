from random import random, randint


class Die:
    def roll(self):
        num = random()
        if num <= .3:
            return 1
        elif num > .3 and num <= .35:
            return 2
        elif num > .35 and num <= .4:
            return 3
        elif num > .4 and num <= .7:
            return 4
        elif num > .7 and num <= .8:
            return 5
        elif num > .8 and num <= 1:
            return 6
