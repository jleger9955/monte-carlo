from coin import Coin
from die import Die


class Experiment:
    def flip_coin_x_times(self, x):
        # returns the probability of head
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x

    def prob_2_heads(self, n):
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    def prob_ththh(self, n):
        c = Coin()
        experiments = [[c.flip() for _ in range(5)] == [0, 1, 0, 1, 1] for _ in range(n)]
        return sum(experiments) / n

    def prob_unfair_hhhh(self, pattern, p, n, flips):
        c = Coin()
        experiments = [[c.unfair_flip(p) for _ in range(flips)] == pattern for _ in range(n)]
        return sum(experiments) / n

    def outcome_4_die_rolls(self, d):

        outcome = []
        # is first roll odd?
        outcome.append(d.roll() % 2 != 0)
        # is second roll = 3
        outcome.append(d.roll() == 3)
        # is third roll 4
        outcome.append(d.roll() == 4)
        # is fourth roll < 3
        outcome.append(d.roll() < 3)
        return outcome

    def prob_unfair_die(self, pattern, n):
        d = Die()
        experiments = [self.outcome_4_die_rolls(d) == pattern for _ in range(n)]
        return sum(experiments) / n
