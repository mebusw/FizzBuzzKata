import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz

import ft

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        ft.featureToggle = False

    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))

    def test_when_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzz().countOff(3))
        self.assertEqual('Fizz', FizzBuzz().countOff(6))

class FizzBuzzFeatureToggleOnTest(unittest.TestCase):
    def test_when_3_then_3_with_feature_toggle(self):
        ft.featureToggle = True
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(3))

if __name__ == "__main__":
    unittest.main()
