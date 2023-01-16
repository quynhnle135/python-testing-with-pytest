import pytest


def test_pass():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip()
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


def test_one():
    assert 1 in [1, 2, 3]


@pytest.mark.skip()
def test_two():
    assert 1 in [2, 3, 4]


def test_three():
    assert "fuzz" in "fuzzbiz"


def test_four():
    a = 3
    b = 4
    assert a < b
