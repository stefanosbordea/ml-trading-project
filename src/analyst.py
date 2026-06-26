from events import SignalEvent

class Analyst:

    def __init__(self):
        self.notebook = None
        self.invested = False
        self.sma = []

    def analyze(self,market_note):
        todays_close = market_note.close

        yesterdays_close = self.notebook
        

        if (self.notebook is None):
            self.notebook = todays_close
            return None
    
        position = todays_close - yesterdays_close
        self.notebook = todays_close
        
        if (position > 0 ):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",strategy = "momentum")
        elif (position < 0):
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "SHORT",strategy = "momentum")

    def buy_and_hold(self,market_note):
        if self.invested is False:
            self.invested = True
            return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",strategy = "buy_and_hold")
        else:
            return None
    
    def sma_crossover(self,market_note):
        self.sma.append(market_note.close)

        avg_50 = 0
        avg_20 = 0

        if len(self.sma) >= 50:
            sum_50 = 0
            sum_20= 0
            for i in range(-1,-51,-1):
                sum_50 += self.sma[i]
           
            for i in range(-1,-21,-1):
                sum_20 += self.sma[i]
            
            avg_50 += sum_50/50
            avg_20 += sum_20/20
            
            if avg_20 > avg_50 :
                return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",strategy = "sma")
            elif avg_20 < avg_50 :
                return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "SHORT",strategy = "sma")
        
        
        





