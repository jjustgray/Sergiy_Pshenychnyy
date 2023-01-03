import unittest
from func_filter import filter_list

class FilterListTest(unittest.TestCase):
    def testNotList(self):
       with self.assertRaises(TypeError):
        filter_list(11)
        
    def testNegativeNumber(self):
       with self.assertRaises(ValueError):
        filter_list([11, 11, -5, 11])

    def  testWork(self):
        self.assertEqual(filter_list([11, 'a', 5, 11]), 
                                    [11, 5, 11])


if __name__ == '__main__':
    unittest.main()
