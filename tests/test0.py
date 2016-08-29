import unittest

class Test0(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(1, 1)

    def test_notequal(self):
        self.assertNotEqual(1, 0)
