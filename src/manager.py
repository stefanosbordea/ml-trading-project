from events import OrderEvent
import math

class Manager :
    def __init__(self,cash):
        self.cash = cash
        self.position = 0
        self.equity_curve = []

    
    def manage(self,signal_note):
        target = None
        equity = self.cash + (self.position * signal_note.price)
        if (signal_note.buy_and_hold == True):
            target = equity
        elif (signal_note.direction == "LONG") :
            target = 0.2 * equity
        elif (signal_note.direction == "SHORT"):
            target = 0
        
        target_units = math.floor(target/signal_note.price)
        order = target_units - self.position
        if order == 0 :
            order = None
        
        if (order is None ):
            return order
        elif (order < 0):
            return OrderEvent(event_type= "ORDER",symbol = signal_note.symbol, date = signal_note.date, direction = "SELL", quantity = abs(order))
        elif (order > 0):
            return OrderEvent(event_type= "ORDER",symbol = signal_note.symbol, date = signal_note.date, direction = "BUY", quantity = abs(order))
    
    def fill_order(self,fill_note):
        fill_cash = (fill_note.price * fill_note.quantity) 
        if (fill_note.direction == "BUY"):
            self.cash -= fill_cash + fill_note.commission
            self.position += fill_note.quantity
        if (fill_note.direction == "SELL"):
            self.cash += fill_cash - fill_note.commission
            self.position -= fill_note.quantity
    
    def mark(self,price):
        equity = self.cash + (self.position * price)
        self.equity_curve.append(equity)
    



        
