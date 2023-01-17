from sandbox.prime_number import is_prime


def test_is_prime_smaller_than_two():
    assert is_prime(1) is False


def test_is_no_prime():
    assert is_prime(4) is False


def test_is_prime():
    assert is_prime(13)