from cards import Card
import pytest

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")


def test_identical():
    c1 = Card(summary="foo", id=123)
    c2 = Card(summary="foo", id=123)
    assert_identical(c1, c2)


def test_identical_fail():
    c1 = Card(summary="foo", id=123)
    c2 = Card(summary="foo", id=321)
    assert_identical(c1, c2)