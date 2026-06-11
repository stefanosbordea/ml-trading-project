from events import SignalEvent

class Analyst:

    def __init__(self):
        self.notebook = None

    def analyze(self,market_note):
        todays_close = market_note.close

        yesterdays_close = self.notebook
        

        if (self.notebook is None):
            self.notebook = todays_close
            return None
        
        position = todays_close - yesterdays_close
        self.notebook = todays_close
        
        if (position > 0 ):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,direction= "LONG")
        elif (position < 0):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,direction= "SHORT")

        
        
        





