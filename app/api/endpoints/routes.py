import logging
import os

from fastapi import APIRouter, HTTPException

from app.api.models.order import OrderRequestData
from app.api.services.fix_socket_service import start_fix_initiator, stop_fix_initiator
from app.api.services.order_service import create_order
from app.api.gateway.broker_gateway import BrokerGatewayApplication

router = APIRouter()
gateway = BrokerGatewayApplication()

initiator = None

configfile = os.path.join(os.getcwd(), "clientLocal.cfg")


@router.on_event("startup")
def startup_event():
    global initiator
    logging.info(f"Config file path: {configfile}")
    initiator = start_fix_initiator(gateway, configfile)
    if initiator is None:
        logging.error("Failed to start FIX initiator")


@router.on_event("shutdown")
def shutdown_event():
    global initiator
    if initiator is not None:
        stop_fix_initiator(initiator)
    else:
        logging.error("No active FIX initiator to stop")


@router.post(
    "/orders/request-quote",
    response_description="Response from the order request",
    responses={400: {"description": "Bad Request"}},
)
def request_quote(order: OrderRequestData):
    global initiator
    if initiator is None:
        raise HTTPException(status_code=500, detail="No active FIX initiator")
    else:
        try:
            response = create_order(gateway, order)
            if response["success"]:
                return {"message": "Message Sent successfully"}
            else:
                logging.error(f"Error creating order")
                raise HTTPException(status_code=400, detail=response["error_message"])
        except Exception as e:
            logging.error(f"Error creating order: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
