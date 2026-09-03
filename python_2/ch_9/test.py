import unittest
import calculator   
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10,50)
        self.assertEqual(result,60)
    def test_sub(self):
            result = calculator.sub(50,10)
            self.assertEqual(result,40)
            
if __name__ == "__main__":
    unittest.main()