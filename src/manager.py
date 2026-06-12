from events import OrderEvent

class Manager :
    def __init__(self,cash):
        self.cash = cash
        self.position = 0
    
    def manage(self,signal_note):
        target = None

        if (signal_note.direction == "LONG") :
            target = 100
        elif (signal_note.direction == "SHORT"):
            target = 0
        
        order = target - self.position
        
        if (order > 0):
            return OrderEvent(event_type= "ORDER",symbol = signal_note.symbol, date = signal_note.date, direction = "BUY", quantity = abs(order))
        elif (order < 0):
            return OrderEvent(event_type= "ORDER",symbol = signal_note.symbol, date = signal_note.date, direction = "SELL", quantity = abs(order))
        elif (order == 0):
            return None

