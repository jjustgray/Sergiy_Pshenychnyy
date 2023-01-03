import unittest
from digital_root import digital_root

class MyTest(unittest.TestCase):
    def testNotInt(self):
       with self.assertRaises(TypeError):
        digital_root('abc')
            
    def testNotStr(self):
       with self.assertRaises(ValueError):
        digital_root(-123)

    def testWork(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(1234), 1)
        self.assertEqual(digital_root(11111), 5)

if __name__ == '__main__':
    unittest.main()
