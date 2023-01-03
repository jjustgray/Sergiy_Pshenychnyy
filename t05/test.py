import unittest
from sort_list import sort_list

class MyTest(unittest.TestCase):
    def testNotString(self):
       with self.assertRaises(TypeError):
        sort_list(123)

    def testWork(self):
        self.assertEqual(sort_list("Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"), "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)")
        self.assertEqual(sort_list("Fred:Corwill;Alfred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"), "(CORWILL, ALFRED)(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)")

if __name__ == '__main__':
    unittest.main()
