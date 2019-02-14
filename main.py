from coin import Coin
from experiment import Experiment
from coin import Coin
from die import Die

e = Experiment()
# print(e.prob_2_heads(2))
# print(e.prob_ththh(10000000))

c = Coin()

# print(e.prob_unfair_hhhh([1, 1, 1, 1], .3, 1000, 4))
'''
d = Die()
for _ in range(10):
    print(e.die_roll())
'''
print(e.prob_unfair_die([1, 1, 1, 1], 1000000))
'''
d = Die()
outcome = []
# is first roll odd?
outcome.append(d.roll() % 2 != 0)
# is second roll = 3
outcome.append(d.roll() == 3)
# is third roll 4
outcome.append(d.roll() == 4)
# is fourth roll < 3
outcome.append(d.roll() < 3)
print(outcome)
print(type(outcome[0]))
print()
'''
