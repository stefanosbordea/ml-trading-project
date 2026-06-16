from dataclasses import dataclass

@dataclass
class MarketEvent:
    event_type: str
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int

@dataclass
class SignalEvent:
    event_type: str
    symbol: str
    date: str
    price: str
    direction: str

@dataclass
class OrderEvent:
    event_type: str
    symbol:str
    date:str
    direction: str
    quantity: int

@dataclass
class FillEvent:
    event_type: str
    symbol:str
    date:str
    price:float 
    quantity:int
    direction: str
    commission: int

    