#!/usr/bin/env python
"""
    test2.py
    - include tests with numpy

"""

import unittest
import numpy as np

print unittest

class Test1(unittest.TestCase):
    def test_numpy(self):
        self.assertFalse( np.all( np.zeros(2) == np.array([0., 0.] ) ) )
        self.assertTrue( np.all( np.zeros(2) == np.array([0., 0.] ) ) )

    def test_almostequal(self):
        self.assertNotEqual(1, 0)
        self.assertAlmostEqual(12.240000000098, 12.240000000099)
if __name__ == '__main__':
    unittest.main()