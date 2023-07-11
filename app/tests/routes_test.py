
from fastapi.testclient import TestClient
from api.main import app


def test_request_quote_no_active_initiator():
    # Create a test client
    client = TestClient(app)

    # Create an order payload
    order_payload = {
        "symbol": "TSLA",
        "quantity": 100,
        "order_type": "MARKET"
    }

    # Send a POST request to the /orders/request-quote endpoint
    response = client.post("/orders/request-quote", json=order_payload)

    # Assert that the response status code is 500
    assert response.status_code == 500

    # Assert that the response message matches the expected message
    assert response.json()["detail"] == "No active FIX initiator"
