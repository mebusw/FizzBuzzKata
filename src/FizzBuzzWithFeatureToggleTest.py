import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_3_then_Fizz(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))
        self.assertEqual('Fizz', FizzBuzz().countOff(3))


if __name__ == "__main__":
    unittest.main()
