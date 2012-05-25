"""
Classes for data presentation

EOD data, realtime data, computed data

Author: vddoan
24/05/2012

"""
import urllib,time,datetime


class AbstractData(object):
    def __init__(self, data_name, date, time, current, open_, high, low, close, volume):
        self.data_name = data_name
        self.date = date
        self.time = time
        self.current = current
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def append(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def to_string(self):
        
    
class EODData(AbstractData):
    def __init__(self, data_name, date, time, open_, high, low, close, volume):
        super(EODData, self).__init__(data_name, date, time, open_, high, low, close, volume)

    def append(self,date, time, open_, high, low, close, volume):
        self.date.append(date.date())
        self.time.append(date.time())
        self.open_.append(float(open_))
        self.high.append(float(high))
        self.low.append(float(low))
        self.close.append(float(close))
        self.volume.append(int(volume))
        
class RealTimeData(AbstractData):
    def __init__(self, data_name, date, time, current):
        super(EODData, self).__init__(data_name, date, time, current)

    def append(self, data_name, date, time, current):
        self.date.append(date.date())
        self.time.append(date.time())
        self.open_.append(float(current))
        

class ComputedData(AbstractData):
