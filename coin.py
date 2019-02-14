from random import randint, random


class Coin:
    def flip(self):
        return randint(0, 1)

    def unfair_flip(self, p):
        # p is the probability of flipping heads
        if random() >= p:
            return 0
        else:
            return 1
