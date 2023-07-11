from unittest.mock import Mock
from api.services.order_service import create_order


def test_create_order():
    # Create a mock gateway
    gateway = Mock()
    order = {
        "symbol": "AAPL",
        "quantity": 100,
        "order_type": "MARKET"
    }

    # Configure the response of the gateway's put_new_order method
    gateway.put_new_order.return_value = {"success": True}

    # Call the create_order function
    response = create_order(gateway, order)

    # Assert that the response is as expected
    assert response == {"success": True}

    # Assert that the gateway's put_new_order method was called with the correct arguments
    gateway.put_new_order.assert_called_once_with(order)
