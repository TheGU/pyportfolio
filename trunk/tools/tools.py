"""
Classes for helpful tools such as StrategyReader (convert from the XML data to create the Python objects)

Author: vddoan
24/05/2012
version:

"""

import xml.dom.minidom as minidom
import xml.etree.ElementTree as etree
from numpy import *
from pyportfolio.core.strategy import *
from pyportfolio.core.estimator import *

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
        self.estimator_dictionnary = {'MovingAverageEstimator': MovingAverageEstimator('MovingAverageEstimator'),
                                     'ExponetialWeightedMovingAverageEstimator': ExponetialWeightedMovingAverageEstimator('ExponetialWeightedMovingAverageEstimator')}
        self.strategy_dictionnary = None
        
      def xml_parse_to_tree(self):
            return etree.parse(self.file_name)

      def get_estimator(self, estimator_name):
            return  self.estimator_dictionnary[estimator_name]
      
      def get_all_strategies(self):
            tree = self.xml_parse_to_tree()
            strategies = [] #[] from numpy
            for node in tree.iter('strategy'):
                  if self.strategy_category == 'voltarget':
                        strategies.append(VolatilityTargetStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None))
                  elif self.strategy_category == 'volbudget':
                        strategies.append(VolatilityBudgetStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None, None))
            return strategies
            
      # A function to converts XML data into native Python object
      def get_strategy(self, criteria_name, criteria_value):
         tree = self.xml_parse_to_tree()
         for node in tree.iter('strategy'):
            node_criteria = node.attrib.get(criteria_name)
            if node_criteria == criteria_value:
                  if self.strategy_category == 'voltarget':
                        sub_node = node.find('estimator')
                        estimator = self.get_estimator(sub_node.attrib.get('name'))
                        return VolatilityTargetStrategy(estimator, node.attrib.get('id'), node.attrib.get('name'), None)
                  elif self.strategy_category == 'volbudget':
                        sub_node = node.find('estimator')
                        estimator = self.get_estimator(sub_node.attrib.get('name'))
                        return VolatilityBudgetStrategy(None, node.attrib.get('id'), node.attrib.get('name'), None, None)
         return None
               

