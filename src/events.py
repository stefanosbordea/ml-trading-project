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
    direction: str


    