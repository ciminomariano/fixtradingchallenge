from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from api.services.fix_socket_service import start_fix_initiator, stop_fix_initiator
from api.services.order_service import create_order
from api.main import app


def test_integration():
    # Mock start_fix_initiator to return a non-None value
    with patch("api.services.fix_socket_service.start_fix_initiator") as mock_start_fix_initiator:
        mock_start_fix_initiator.return_value = MagicMock()

        # Create a test client
        client = TestClient(app)

        # Test case 1: test_start_fix_initiator
        # Perform assertions within the test_start_fix_initiator function

        # Test case 2: test_create_order
        # Mock the gateway and configure the response of the put_new_order method
        gateway = MagicMock()
        gateway.put_new_order.return_value = {"success": True}

        # Call the create_order function
        response = create_order(gateway, {"symbol": "AAPL", "quantity": 100, "order_type": "MARKET"})

        # Assert that the response is as expected
        assert response == {"success": True}

        # Test case 3: test_request_quote_no_active_initiator
        # Send a POST request to the /orders/request-quote endpoint
        response = client.post("/orders/request-quote", json={"symbol": "TSLA", "quantity": 100, "order_type": "MARKET"})

        # Assert that the response status code is 500
        assert response.status_code == 500

        # Assert that the response message matches the expected message
        assert response.json()["detail"] == "No active FIX initiator"
