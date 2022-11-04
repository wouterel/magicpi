import magicpi as mp
import numpy as np


def test_value():
    assert np.abs(np.sin(mp.pi())) < 1e-15

