from fastapi import APIRouter, HTTPException

from api.models.order import OrderRequestData
from api.services.fix_socket_service import start_fix_initiator, stop_fix_initiator
from api.services.order_service import create_order
from app.api.gateway.broker_gateway import BrokerGatewayApplication

router = APIRouter()
gateway = BrokerGatewayApplication()

initiator = None


@router.on_event("startup")
def startup_event():
    global initiator
    initiator = start_fix_initiator(gateway)


@router.on_event("shutdown")
def shutdown_event():
    stop_fix_initiator(initiator)


@router.post(
    "/orders/request-quote",
    response_description="Response from the order request",
    responses={400: {"description": "Bad Request"}},
)
def request_quote(order: OrderRequestData):
    try:
        response = create_order(gateway, order)

        if response["success"]:
            return {"message": "Message Sent successfully"}
        else:
            raise HTTPException(status_code=400, detail=response["error_message"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
