import pytest

from sandbox.app import User


def test_create_user():
    user = User(first_name="Quinn", last_name="Le", id=123, dob="5/13/2001")
    assert user.first_name == "Quinn"
    assert user.last_name == "Le"
    assert user.dob == "5/13/2001"
    assert user.get_user_id() == 123


def test_create_user_without_input():
    user = User()
    assert user.first_name is None
    assert user.last_name is None
    assert user.dob is None
    assert user.get_user_id() == 0


def test_user_str():
    user = User(first_name="Quinn", last_name="Le", id=123, dob="5/13/2001")
    assert user.__str__() == "User's full name: Quinn Le"


def test_able_to_enroll_health_insurance():
    with pytest.raises(Exception):
        user = User(first_name="Quinn", last_name="Le", id=123, dob="5/13/2001")
        user.able_to_enroll_health_insurance(-10)

    user1 = User(first_name="Quinn", last_name="Le", id=123, dob="5/13/2001")
    user2 = User(first_name="Phong", last_name="Le", id=123, dob="6/13/1950")
    assert user1.able_to_enroll_health_insurance(age=21) is False
    assert user2.able_to_enroll_health_insurance(age=72) is True


# def test_able_to_enroll_health_insurance_raise():
#     user = User(first_name="Quinn", last_name="Le", id=123, dob="5/13/2001")
#     with pytest.raises(Exception):
#         user.able_to_enroll_health_insurance(-10)
