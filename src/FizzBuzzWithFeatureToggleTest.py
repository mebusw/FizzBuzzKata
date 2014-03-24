import unittest

from FizzBuzzWithFeatureToggle import FizzBuzzWithBodyMovement


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzzWithBodyMovement().countOff(1))
        self.assertEqual(2, FizzBuzzWithBodyMovement().countOff(2))

    def test_when_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzzWithBodyMovement().countOff(3))


if __name__ == "__main__":
    unittest.main()
