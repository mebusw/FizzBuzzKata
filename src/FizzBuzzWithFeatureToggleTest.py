import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz

import ft

class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))

    def test_when_3_then_Fizz(self):
        ft.featureToggle = False
        self.assertEqual('Fizz', FizzBuzz().countOff(3))

    def test_when_3_then_3_with_feature_toggle(self):
        ft.featureToggle = True
        self.assertEqual(3, FizzBuzz().countOff(3))

if __name__ == "__main__":
    unittest.main()
