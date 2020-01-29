import unittest
import calc


#class TestUser(unittest.TestCase):

 #   def test_init


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3,2), 9)



if __name__ == '__main__':
    unittest.main()