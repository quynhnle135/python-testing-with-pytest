import pytest
from cards import Card

def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "nick")
    if c1 != c2:
        pytest.fail("they don't match!")
