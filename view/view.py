"""
Classes for plotting panels

Based on observer/observable and factory method pattern

Author: vddoan
24/05/2012
version:

"""

from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
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
        self.quotes = None # multi-dimension quotes
        self.x_quotes = None # x-axe quotes
        self.y_quotes = None # y-axe quotes
        self.z_quotes = None # z-axe quotes
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.grid = grid
        self.plotting_type_dictionnary = {'line': None,
                                              'dot': 'r.',
                                              'line-dot':'o-',
                                              'candle': 'candlestick'   
                                              }
        self.plotting_dimension_dictionnary = None
        
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
      
      def get_quotes_via_yahoo_loader(self, ticker_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

      def get_quotes_via_google_loader(self, ticker_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

      def get_quotes_via_local_csv(self, csv_file, file_type):
            raise NotImplementedError("Subclass must implement abstract method")

      # map multi-dimension quotes to 2-dimension quotes
      def set_xyz_quotes(self):
            raise NotImplementedError("Subclass must implement abstract method")
      
      def get_plotting_type(self, _type):
            return self.plotting_type_dictionnary[_type]

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
            if self.criteria == "normal":
                  plotter = NormalPlottingPanel(None, None, self.xlabel, self.ylabel, self.title, self.grid)
                  return plotter
            else:
                  return 0


class NormalPlottingPanel(AbstractPlottingPanel):
      
      def __init__(self, figure, widgets, xlabel, ylabel, title, grid):
        super(NormalPlottingPanel, self).__init__(figure, widgets, xlabel, ylabel, title, grid)

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
            
      def get_quotes_via_yahoo_loader(self, ticker_name, start_date, end_date):
            self.quotes = HistoricalYahooDataLoader(ticker_name, start_date, end_date).load()
            self.plotting_dimension_dictionnary = {'date': self.quotes.d,
                                                   'year': self.quotes.year,
                                                   'month': self.quotes.month,
                                                   'day': self.quotes.day,
                                                   'open': self.quotes.open,
                                                   'close':self.quotes.close,
                                                   'low': self.quotes.low,
                                                   'high': self.quotes.high,
                                                   'volume' : self.quotes.volume,
                                                   'adj-close' : self.quotes.aclose,
                                                   'null' : None
                                                   }
            if len(self.quotes) == 0:
                raise SystemExit
            else:
                  return self.quotes

      def get_quotes_via_random_generator(self):
            return 0

      def get_quotes_via_local_csv(self, csv_file, start_date, end_date):
            #datafile = csv.reader(open('csv_file', 'rb'), delimiter=',', quotechar='|')
            datafile = cbook.get_sample_data(csv_file, asfileobj=False)
            self.quotes = mlab.csv2rec(datafile)

            #print self.quotes.dtype.names #names = list of columns name
            
            self.plotting_dimension_dictionnary = {'date': self.quotes.date,
                                                   'open': self.quotes.open,
                                                   'close':self.quotes.close,
                                                   'low': self.quotes.low,
                                                   'high': self.quotes.high,
                                                   'volume' : self.quotes.volume,
                                                   'adj-close' : self.quotes.adj_close,
                                                   'null' : None
                                                   }
            
            if len(self.quotes) == 0:
                raise SystemExit
            else:
                  return self.quotes

      # make x,y,z quotes
      def set_xyz_quotes(self, x_param, y_param, z_param):
            if x_param != 'null':
                  self.x_quotes = self.plotting_dimension_dictionnary[x_param]
            else:
                  self.x_quotes = None
            if y_param != 'null':
                  self.y_quotes = self.plotting_dimension_dictionnary[y_param]
            else:
                  self.y_quotes = None
            if z_param != 'null':
                  self.z_quotes = self.plotting_dimension_dictionnary[z_param]
            else:
                  self.z_quotes = None
            
      def plot(self, plot_type):
            ''' check if quotes data is empty or not '''
            if len(self.quotes) == 0:
                raise SystemExit

            self.setup_figure()
            self.setup_date_format()

            if plot_type == 'candle':
                  candlestick(self.ax, self.quotes, width=0.6)
            else:
                  #plt.plot(self.quotes.d, self.quotes.open, color='red', lw=2)
                  #plt.plot(self.quotes.d, self.quotes.open, self.get_plotting_type(plot_type))
                  plt.plot(self.x_quotes, self.y_quotes, self.get_plotting_type(plot_type))
            
            self.setup_label_format()
            plt.show()

#class TimeSeriePlottingPanel(AbstractPlottingPanel):
#class HistogramPlottingPanel(AbstractPlottingPanel):

            

