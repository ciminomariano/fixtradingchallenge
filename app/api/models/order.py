from pydantic import BaseModel, Field, validator

from api.models.Enums import SymbolType, OrderType


class OrderRequest(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock")
    quantity: int = Field(..., gt=0, description="Order quantity")
    order_type: str = Field(..., description="Type of the order")

    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "TSLA",
                "quantity": 10,
                "order_type": "market"
            }
        }


class OrderRequestData(BaseModel):
    symbol: SymbolType = Field(..., description="Symbol of the stock")
    quantity: int = Field(..., gt=0, description="Order quantity")
    order_type: OrderType = Field(..., description="Type of the order")

    @validator('symbol', pre=True)
    def validate_symbol(cls, symbol):
        # Convert the symbol to uppercase
        symbol = symbol.upper()
        # If the validation fails, raise a ValueError exception
        if symbol not in SymbolType.__members__:
            valid_symbols = ', '.join([m.value for m in SymbolType])
            raise ValueError(f"Invalid symbol. Possible values are: {valid_symbols}")
            # Add more validations if necessary

        return symbol

    @validator('quantity', pre=True)
    def validate_quantity(cls, quantity):
        # Perform quantity validation here
        # You can use conditionals, ranges, etc.
        # If the validation fails, raise a ValueError exception
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        # Add more validations if necessary

        return quantity

    @validator('order_type', pre=True)
    def validate_order_type(cls, order_type):

        # Convert order type to uppercase
        order_type = order_type.upper()
        if order_type not in OrderType.__members__:
            valid_order_types = ', '.join([m.value for m in OrderType])
            raise ValueError(f"Invalid order type. Possible values are: {valid_order_types}")
        # Add more validations if needed

        return order_type
