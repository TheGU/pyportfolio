from matplotlib.finance import quotes_historical_yahoo

class AbstractLoader(object):
      def __init__(self, ticker_name, start_date, end_date):
        self.ticker_name = ticker_name
        self.start_date = start_date
        self.end_date = end_date

      def load(self):
            raise NotImplementedError("Subclass must implement abstract method")

class HistoricalYahooDataLoader(AbstractLoader):
      def __init__(self, ticker_name, start_date, end_date):
        super(HistoricalYahooDataLoader, self).__init__(ticker_name,start_date, end_date)

      def load(self):
            return quotes_historical_yahoo(self.ticker_name, self.start_date, self.end_date, asobject=True, adjusted=True)

class HistoricalGoogleDataLoader(AbstractLoader):
      def __init__(self, ticker_name, start_date, end_date):
        super(HistoricalGoogleDataLoader, self).__init__(ticker_name,start_date, end_date)




        
      
