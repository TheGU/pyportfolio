from pyportfolio.view.view import *
from pyportfolio.core.strategy import *
from pyportfolio.tools.tools import *

if __name__ == '__main__':
##      date1 = (2010, 2, 1)
##      date2 = (2010, 4, 12 )
##      ticker = 'GOOG'
##      plotter = PlottingPanelFactory('timeserie', 'date time', 'Google stock price', 'Daily Google stock price plotter', True).get_panel()
##      plotter.set_quote_data_via_yahoo_loader(ticker, date1, date2)
##      plotter.plot('continuos')

      reader = StrategyReader('vol_target_strategies.xml', 'voltarget')
      
      strategy = reader.get_strategy("id","1")
      
      print strategy.name

      reader = StrategyReader('vol_budget_strategies.xml', 'volbudget')
      
      strategy = reader.get_strategy("name","Vol Budget 2")
      
      print strategy.id

      reader = StrategyReader('vol_budget_strategies.xml', 'volbudget')
      
      strategies = reader.get_all_strategies()

      for strategy in strategies:
            print strategy.name
