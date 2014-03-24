import unittest

from FizzBuzzWithFeatureToggle import FizzBuzzWithFeatureToggle


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_3_then_Fizz(self):
        self.assertEqual(1, FizzBuzzWithFeatureToggle().countOff(1))
        self.assertEqual(2, FizzBuzzWithFeatureToggle().countOff(2))
        self.assertEqual('Fizz', FizzBuzzWithFeatureToggle().countOff(3))


if __name__ == "__main__":
    unittest.main()
