from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick, plot_day_summary, candlestick2

class AbstractViewPanel(object):
      def __init__(self, data_name, start_date, end_date):
        self.data_name = data_name
        self.start_date = start_date
        self.end_date = end_date

      def update():
            raise NotImplementedError("Subclass must implement abstract method")

      def plottingFromLocalFile(data_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

      def plottingFromWebFile(data_name, start_date, end_date):
            raise NotImplementedError("Subclass must implement abstract method")

class NormalViewPanel(AbstractViewPanel):
      def __init__(self, data_name, start_date, end_date):
        super(NormalViewPanel, self).__init__(data_name,start_date, end_date)

      def update():
            return 0

##      def plottingFromLocalFile(file_name, start_date, end_date):
##            return 0

      def plottingFromWebFile(self):
            mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
            alldays    = DayLocator()              # minor ticks on the days
            weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
            dayFormatter = DateFormatter('%d')      # Eg, 12

            quotes = quotes_historical_yahoo(self.data_name, self.start_date, self.end_date)

            print quotes

            if len(quotes) == 0:
                raise SystemExit

            fig = figure()
            fig.subplots_adjust(bottom=0.2)
            ax = fig.add_subplot(111)
            ax.xaxis.set_major_locator(mondays)
            ax.xaxis.set_minor_locator(alldays)
            ax.xaxis.set_major_formatter(weekFormatter)
            #ax.xaxis.set_minor_formatter(dayFormatter)

            #plot_day_summary(ax, quotes, ticksize=3)
            candlestick(ax, quotes, width=0.6)

            ax.xaxis_date()
            ax.autoscale_view()
            setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')

            show()


#class ChartViewPanel(AbstractViewPanel):
