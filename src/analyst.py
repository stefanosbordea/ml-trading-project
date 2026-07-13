from events import SignalEvent
import pandas as pd

class Analyst:

    def __init__(self):
        self.notebook = None
        self.invested = False
        self.sma = []
        self.twelve_one = []

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
    
    def find_target(self,list,target):
        for entry in reversed(list):
            if entry[0] <= target:
                return entry[1]
        return None

    def twelve_minus_one(self,market_note):
        self.twelve_one.append((market_note.date,market_note.close))

        year = market_note.date - pd.DateOffset(months = 12)
        month = market_note.date - pd.DateOffset(months = 1)

        price_year = self.find_target(self.twelve_one,year)
        price_month = self.find_target(self.twelve_one,month)

        if (price_year is not None and price_month is not None):

            s = ((price_month - price_year) / price_year) * 100
            if s > 0:
                return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "LONG",strategy = "12-1")
            elif s < 0:
                return SignalEvent(event_type="SIGNAL",symbol = market_note.symbol,date = market_note.date,price = market_note.close,direction= "SHORT",strategy = "12-1")
        else:
            return None
    
    
        


        
        





