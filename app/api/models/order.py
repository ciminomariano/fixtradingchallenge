from pydantic import BaseModel


class OrderRequest(BaseModel):
    symbol: str
    quantity: int
    order_type: str

