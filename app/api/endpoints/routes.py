from fastapi import APIRouter, HTTPException
from app.api.models.order import OrderRequest
from app.api.services.socket_conector import start_socket


router = APIRouter()


@router.post("/orders/request-quote")
def request_quote(order: OrderRequest):
    try:
        response = start_socket(order)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
