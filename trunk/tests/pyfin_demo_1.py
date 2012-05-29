from pyportfolio.view.view import *

if __name__ == '__main__':
      date1 = (2010, 2, 1)
      date2 = (2010, 4, 12 )
      ticker = 'GOOG'
      plotter = PlottingPanelCreator('timeserie', 'date time', 'Google stock price', 'Daily Google stock price plotter', True).get_panel()
      plotter.set_quote_data_via_yahoo_loader(ticker, date1, date2)
      plotter.plot('continuos')
