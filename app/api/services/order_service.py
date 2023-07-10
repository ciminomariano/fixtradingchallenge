from api.models.order import OrderRequest
from api.gateway.broker_gateway import BrokerGatewayApplication


def request_quote_service(order: OrderRequest):
    Broker = BrokerGatewayApplication()
    Broker.put_new_order(order)
