from events import FillEvent

class Broker:

    def __init__(self,commission,slippage):
        self.slippage = slippage
        self.commission = commission
        self.pending = None

    def pending_order(self,order_event):
        self.pending = order_event
        

    def trade(self,market_note):
        if (self.pending is not None):
            if (self.pending.direction == "BUY"):
                price = market_note.open + (market_note.open * self.slippage)
                fill = FillEvent(event_type = "FILL", symbol = self.pending.symbol,date = market_note.date, price = price, quantity = self.pending.quantity, direction = self.pending.direction, commission = self.pending.quantity * price * self.commission )
            else :
                price = market_note.open -(market_note.open * self.slippage)
                fill = FillEvent(event_type = "FILL", symbol = self.pending.symbol,date = market_note.date, price = price, quantity = self.pending.quantity, direction = self.pending.direction, commission = self.pending.quantity * price * self.commission )
            self.pending = None
            return fill
        else:
            return None
    

        

