#!/usr/bin/env python
"""
    test0.py

"""

import unittest

print unittest

class Test0(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(1, 1)

    def test_notequal(self):
        self.assertNotEqual(1, 0)

if __name__ == '__main__':
    unittest.main()