from unittest.mock import Mock

from sandbox.employee import *


def test_create_employee_with_no_value():
    e1 = Employee()
    assert e1.name is None
    assert e1.department is None


def test_create_employee():
    e1 = Employee("Quinn", "IT")
    assert e1.name == "Quinn"
    assert e1.department == "IT"


def test_employee_get_promotion():
    e1 = Employee()
    manager = Mock()
    manager.decide.return_value = True
    assert e1.get_promotion(manager) is True
