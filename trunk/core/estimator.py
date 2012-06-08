"""
Classes for estimator (used in strategy classes)

Author: vddoan
24/05/2012
version:

"""


class AbstractEstimator(object):
      def __init__(self, name):
            self.name = name


class MovingAverageEstimator(AbstractEstimator):
      def __init__(self, name):
            super(MovingAverageEstimator, self).__init__(name)

      def get_volatility(self):
            
            return 0
      
class ExponetialWeightedMovingAverageEstimator(AbstractEstimator):
      def __init__(self, name):
            super(ExponetialWeightedMovingAverageEstimator, self).__init__(name)

      def get_volatility(self):
            return 0
