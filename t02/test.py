import unittest
from non_repeat import first_non_repeating_letter

class MyTest(unittest.TestCase):
    def testNotStr(self):
       with self.assertRaises(TypeError):
        first_non_repeating_letter(123)

    def  testWork(self):
        self.assertEqual(first_non_repeating_letter('sTress'), 'T')
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('AAAaaabBccDef'), 'D')


if __name__ == '__main__':
    unittest.main()
