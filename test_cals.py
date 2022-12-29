import Cals
import unittest
class testCalc(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(Cals.addition(10,5),15)
        self.assertEqual(Cals.addition(10,6),16)

    def test_subtraction(self):
        self.assertEqual(Cals.subtraction(10,3),7)
    def test_multiplication(self):
        self.assertEqual(Cals.multiplication(5,5),25)
    def test_division(self):
        self.assertEqual(Cals.division(10,5),2)

if __name__=="__main__":
    unittest.main()