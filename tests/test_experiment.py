from coin import Coin
from experiment import Experiment
from pytest import approx


def test_probability_of_a_head():
    e = Experiment()
    p = e.flip_coin_x_times(100000)
    assert p == approx(0.5, rel=0.01)


def test_probability_of_hh():
    e = Experiment()
    p = e.prob_2_heads(100000)
    assert p == approx(0.25, rel=.01)


def test_probability_of_ththh():
    e = Experiment()
    p = e.prob_ththh(1000000)
    assert p == approx((0.5)**5, rel=.01)


def test_probability_of_unfair_hhhh():
    e = Experiment()
    p = e.prob_unfair_hhhh([1, 1, 1, 1], .3, 1000000, 4)
    assert p == approx((0.3)**4, rel=.01)


def test_probability_unfair_die_roll():
    e = Experiment()
    p = e.prob_unfair_die([1, 1, 1, 1], 1000000)
    assert p == approx(.45 * .05 * .30 * .35, rel=.01)
