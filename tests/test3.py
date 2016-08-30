"""

test3.py


"""


import unittest


class Test4(unittest.TestCase):

    def testa(self):
        a = 1
        b = 2
        self.assertEqual(type(a), type(b))

    def testb(self):
        a = 1
        b = 2.2
        self.assertEqual(type(a), type(b))

