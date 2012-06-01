"""

Set of unittests for tools

author: vddoan
date: 01/06/2012

"""

import unittest
from pyportfolio.tools.tools import *
from pyportfolio.core.strategy import *

class StrategyReaderTest(unittest.TestCase):

    def setUp(self):
        self.strategyReader = StrategyReader('../bnp_strategies.xml', 'bnp')

    def test_get_strategy(self):
        strategy = self.strategyReader.get_strategy("id","1")
        self.assertTrue(isinstance(strategy, BNPStrategy), True)

    def test_get_strategies(self):
        strategies = self.strategyReader.get_all_strategies()
        self.assertEqual(len(strategies), 3)
        
    def tearDown(self):
        self.strategyReader.__del__()
        
if __name__ == '__main__':
    unittest.main()
