from fastapi import APIRouter, HTTPException
from app.api.services.order_service import OrderService
from app.api.models.order import OrderRequest

router = APIRouter()
order_service = OrderService()


@router.post("/orders/request-quote")
def request_quote(order: OrderRequest):
    try:
        response = order_service.request_quote(order)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
