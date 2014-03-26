import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz


class FizzBuzzWithBodyMovement():
    def countOff(self, n):
        pass


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))

    def test_when_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzz().countOff(3))

    def test_when_3_then_FizzAndTouchHead(self):
        self.assertEqual('FizzAndTouchHead', FizzBuzzWithBodyMovement().countOff(3))


if __name__ == "__main__":
    unittest.main()
