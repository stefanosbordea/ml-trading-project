from events import FillEvent

class Broker:

    def __init__(self,commission):
        self.commission = commission
        self.pending = None

    def pending_order(self,order_event):
        self.pending = order_event
        

    def trade(self,market_note):
        if (self.pending is not None):
            fill = FillEvent(event_type = "FILL", symbol = self.pending.symbol,date = market_note.date, price = market_note.open, quantity = self.pending.quantity, direction = self.pending.direction, commission = self.commission)
            self.pending = None
            return fill
        else:
            return None
    

        

