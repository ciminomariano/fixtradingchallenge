from app.api.gateway.broker_gateway import BrokerGatewayApplication
from app.api.models.order import OrderRequest
from fastapi import HTTPException


class OrderService:
    def __init__(self):
        self.broker_gateway = BrokerGatewayApplication()

    def make_test_order(self, order: OrderRequest):
        self.broker_gateway.request_quote(order.getSymbol())

    def request_quote(self, order: OrderRequest):
        try:
            self.broker_gateway.request_quote(order)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def start_gateway(self, config_file):
        self.broker_gateway.main(config_file)
