# simpler syntax for defining classes
# comes with free equality check and a good string representation
# It's easy to add ordering too, <, > etc
from dataclasses import make_dataclass
Stock = make_dataclass("Stock", "symbol", "current", "high", "low")
stock = Stock("FB", 177.46, high=178.67, low=175.79)

class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

stock_reg_class = Stock("FB", 177.46, high=178.67, low=175.79)

from dataclasses import dataclass

@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float

@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


stock_ordered1 = StockDecorated("FB", 177.46, high=178.67, low=175.79)
stock_ordered2 = StockOrdered("FB")
stock_ordered3 = StockDecorated("FB", 178.42, high=179.28, low=176.39)