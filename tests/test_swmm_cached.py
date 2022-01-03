
from swmm_cached import longest
from swmm_cached import main


def test_main():
    pass


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
