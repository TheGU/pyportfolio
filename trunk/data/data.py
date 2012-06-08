"""
Classes for data presentation

EOD data, realtime data, computed data

Author: vddoan
24/05/2012
version:

"""
import urllib,time,datetime


class AbstractData(object):
    def __init__(self, data_name, date, time, current, open_, high, low, close, volume):
        self.data_name = data_name # for all types of data
        self.date = date # for all types of data
        self.time = time # for all types of data
        self.current = current # for realtime data
        self.bid = bid # for realtime data
        self.ask = ask # for realtime data
        self.open_ = open_ # for EOD data
        self.high = high # for EOD data
        self.low = low # for EOD data
        self.close = close # for EOD data
        self.volume = volume # for EOD data

    def append(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def to_string(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
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
        super(EODData, self).__init__(data_name, date, time, current, bid, ask)

    def append(self, data_name, date, time, current):
        self.date.append(date.date())
        self.time.append(date.time())
        self.current.append(float(current))
        self.bid.append(float(bid))
        self.ask.append(float(ask))
        

class ComputedData(AbstractData):
