from fastapi.testclient import TestClient
from api.main import app
from api.services.fix_socket_service import start_fix_initiator, stop_fix_initiator
from api.gateway.broker_gateway import BrokerGatewayApplication

client = TestClient(app)


def test_create_order():
    # Inicializar el iniciador de FIX
    gateway = BrokerGatewayApplication()
    initiator = start_fix_initiator(gateway)

    # Realizar la solicitud de prueba
    order_data = {
        "symbol": "TSLA",
        "order_type": "MARKET",
        "quantity": 100
    }
    response = client.post("/orders/request-quote", json=order_data)

    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json() == {"message": "Message Sent successfully"}

    # Detener el iniciador de FIX
    stop_fix_initiator(initiator)
