from enum import Enum


class SymbolType(str, Enum):
    TSLA = "TSLA"
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOG = "GOOG"
    AMZN = "AMZN"
    FB = "FB"
    NFLX = "NFLX"
    IBM = "IBM"
    INTC = "INTC"
    NVDA = "NVDA"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
