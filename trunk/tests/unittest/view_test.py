"""

Set of unittests for view

author: vddoan
date: 01/06/2012

"""

import unittest
from pyportfolio.view.view import *

class PlottingPanelFactoryTest(unittest.TestCase):

    def setUp(self):
        self.plottingPanelFactory = PlottingPanelFactory('timeserie', None, None, None, True)

    def test_get_panel(self):
        panel = self.plottingPanelFactory.get_panel()
        self.assertTrue(isinstance(panel, TimeSeriePlottingPanel), True)
        
    def tearDown(self):
        self.plottingPanelFactory.__del__()
        
if __name__ == '__main__':
    unittest.main()
