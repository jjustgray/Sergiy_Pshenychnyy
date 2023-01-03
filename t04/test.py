import unittest
import array as arr
from target_sum import target_sum

class MyTest(unittest.TestCase):
    def testNotNdarray(self):
       with self.assertRaises(TypeError):
        target_sum(0, 0, 0)
            
    def testBadTarget(self):
       with self.assertRaises(TypeError):
        target_sum(arr.array('i', [0, 1, 0, 1]), 'abc')

    def testWork(self):
        self.assertEqual(target_sum(arr.array('i', [0, 1, 0, 0]), 1), 3)
        self.assertEqual(target_sum(arr.array('i', [0, 0, 0, 0]), 0), 6)
        self.assertEqual(target_sum(arr.array('i', [1, 3, 6, 2, 2, 0, 4, 5]), 5), 4)

if __name__ == '__main__':
    unittest.main()
