from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import *
from matplotlib.widgets import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick, plot_day_summary, candlestick2
from pyportfolio.connectivity.loader import *

""" Using Factory Method pattern for creating plotters """
class AbstractPlottingPanel(object):

      def __init__(self, figure, widgets, xlabel, ylabel, title, grid):
        self.figure = figure
        self.widgets = widgets
        self.ax = None
        self.quotes = None
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.grid = grid

      def __del__(self):
            class_name = self.__class__.__name__
            
      ''' For observer pattern '''  
      def update():
            raise NotImplementedError("Subclass must implement abstract method")

      def setup_figure(self):
            raise NotImplementedError("Subclass must implement abstract method")

      def plot(self, plot_type):
            raise NotImplementedError("Subclass must implement abstract method")

      def setup_date_format(self):
            raise NotImplementedError("Subclass must implement abstract method")

      def setup_label_format(self):
            raise NotImplementedError("Subclass must implement abstract method")
      
      def set_quote_data_via_yahoo_loader(self, ticker_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

      def set_quote_data_via_google_loader(self, ticker_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

      def set_quote_data_via_local_file(self, file_name, file_type):
            raise NotImplementedError("Subclass must implement abstract method")
            
''' Factory '''
class PlottingPanelFactory(object):
      def __init__(self, criteria, xlabel, ylabel, title, grid):
            self.criteria = criteria
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.title = title
            self.grid = grid

      def __del__(self):
            class_name = self.__class__.__name__
            
      def get_panel(self):
            if self.criteria == "timeserie":
                  plotter = TimeSeriePlottingPanel(None, None, self.xlabel, self.ylabel, self.title, self.grid)
                  return plotter
            else:
                  return 0
      

class TimeSeriePlottingPanel(AbstractPlottingPanel):
      
      def __init__(self, figure, widgets, xlabel, ylabel, title, grid):
        super(TimeSeriePlottingPanel, self).__init__(figure, widgets, xlabel, ylabel, title, grid)

      def update():
            return 0

      def setup_figure(self):
            self.figure = plt.figure()
            self.ax = self.figure.add_subplot(111)
            self.ax.set_xlabel(self.xlabel)
            self.ax.set_ylabel(self.ylabel)
            self.ax.set_title(self.title)
            self.ax.grid(self.grid)
     
      def setup_date_format(self):
            years    = mdates.YearLocator()   # every year
            months   = mdates.MonthLocator()  # every month
            yearsFormatter = mdates.DateFormatter('%Y')
            mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
            alldays    = DayLocator()               # minor ticks on the days
            weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
            dayFormatter = DateFormatter('%d')      # Eg, 12
            
            self.ax.xaxis_date()
            self.ax.autoscale_view()
            self.ax.xaxis.set_major_locator(mondays)
            self.ax.xaxis.set_minor_locator(alldays)
            self.ax.xaxis.set_major_formatter(weekFormatter)

      def setup_label_format(self):
            setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')
            
      def set_quote_data_via_yahoo_loader(self, ticker_name, start_date, end_date):
            self.quotes = HistoricalYahooDataLoader(ticker_name, start_date, end_date).load()
            if len(self.quotes) == 0:
                raise SystemExit
            else:
                return self.quotes

      def set_quote_data_via_random_generator(self):
            return 0
            
      def plot(self, plot_type):
            ''' check if quotes data is empty or not '''
            if len(self.quotes) == 0:
                raise SystemExit

            self.setup_figure()
            self.setup_date_format()
            
            if plot_type == 'candle':
                  candlestick(self.ax, self.quotes, width=0.6)
            elif plot_type == 'continuos':
                  plt.plot(self.quotes.d, self.quotes.open, color='red', lw=2)
            else:
                  raise SystemExit
            
            self.setup_label_format()
            plt.show()
                        
#class HistogramPlottingPanel(AbstractPlottingPanel):

            

