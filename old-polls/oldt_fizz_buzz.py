import unittest
from fizz_buzz import solution

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_4(self):
        self.assertEqual(solution(4),4)
    def test_fizz_buzz_7(self):
        self.assertEqual(solution(7),7)
    def test_fizz_buzz_3(self):
        self.assertEqual(solution(3),'fizz')    
    def test_fizz_buzz_6(self):
        self.assertEqual(solution(6),'fizz')            
    def test_fizz_buzz_5(self):
        self.assertEqual(solution(5),'buzz')                    
    def test_fizz_buzz_10(self):
        self.assertEqual(solution(10),'buzz')                            
    def test_fizz_buzz_15(self):
        self.assertEqual(solution(15),'fizz-buzz')                                    
    def test_fizz_buzz_30(self):
        self.assertEqual(solution(30),'fizz-buzz')                                            


unittest.main()