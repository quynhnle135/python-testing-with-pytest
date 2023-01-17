from unittest.mock import Mock
from mock.order import Order


def test_order_is_filled():
    order = Order("Talisker", 50)
    warehouse = Mock()
    warehouse.has_inventory.return_value = True
    warehouse.remove.return_value = None
    order.fill(warehouse=warehouse)
    assert order.is_filled()


def test_order_is_not_filled():
    order = Order("Brush", 100)
    warehouse = Mock()
    warehouse.has_inventory.return_value = False
    order.fill(warehouse=warehouse)
    assert order.is_filled() == False
