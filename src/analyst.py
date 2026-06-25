from events import SignalEvent

class Analyst:

    def __init__(self):
        self.notebook = None
        self.invested = False

    def analyze(self,market_note):
        todays_close = market_note.close

        yesterdays_close = self.notebook
        

        if (self.notebook is None):
            self.notebook = todays_close
            return None
    
        
        position = todays_close - yesterdays_close
        self.notebook = todays_close
        
        if (position > 0 ):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",buy_and_hold = False)
        elif (position < 0):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "SHORT",buy_and_hold = False)

    def buy_and_hold(self,market_note):
        if self.invested is False:
            self.invested = True
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",buy_and_hold = True)
        else:
            return None
        
        





