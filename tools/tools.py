import xml.dom.minidom as minidom
import xml.etree.ElementTree as etree
from pyportfolio.core.strategy import *
from numpy import *

class Reader(object):

      def __init__(self, file_name):
            self.file_name = file_name

      def __del__(self):
            class_name = self.__class__.__name__

      def xml_parse_to_tree(self):
            raise NotImplementedError("Subclass must implement abstract method")
      
class StrategyReader(Reader):

      def __init__(self, file_name, strategy_category):
        super(StrategyReader, self).__init__(file_name)
        self.strategy_category = strategy_category

      def xml_parse_to_tree(self):
            return etree.parse(self.file_name)
      
      def get_all_strategies(self):
            tree = self.xml_parse_to_tree()
            strategies = [] #[] from numpy
            for node in tree.iter('strategy'):
                  if self.strategy_category == 'bnp':
                        strategies.append(BNPStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None, None, None))
                  elif self.strategy_category == 'sg':
                        strategies.append(SGStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None))
            return strategies
            
      # A function to converts XML data into native Python object
      def get_strategy(self, criteria_name, criteria_value):
         tree = self.xml_parse_to_tree()
         for node in tree.iter('strategy'):
            node_criteria = node.attrib.get(criteria_name)
            if node_criteria == criteria_value:
                  if self.strategy_category == 'bnp':
                        return BNPStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None, None, None)
                  elif self.strategy_category == 'sg':
                        return SGStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None)
         return None
               
