from pyfin.view.view import *

if __name__ == '__main__':
      date1 = (2004, 2, 1)
      date2 = (2004, 4, 12 )
      view = NormalViewPanel('INTC', date1, date2)
      view.plottingFromWebFile()
