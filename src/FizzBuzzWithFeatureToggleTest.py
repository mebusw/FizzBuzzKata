import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz

class FizzBuzzTestBodyMovementToggleOffTest(unittest.TestCase):
    def setUp(self):
        FizzBuzz.featureToggleBodyMovement = False

    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))

    def test_when_multiple_of_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzz().countOff(3))
        self.assertEqual('Fizz', FizzBuzz().countOff(6))

    def test_when_multiple_of_5_then_Buzz(self):
        self.assertEqual('Buzz', FizzBuzz().countOff(5))
        self.assertEqual('Buzz', FizzBuzz().countOff(10))

    def test_when_multiple_of_3_or_5_then_FizzBuzz(self):
        self.assertEqual('FizzBuzz', FizzBuzz().countOff(15))
        self.assertEqual('FizzBuzz', FizzBuzz().countOff(30))

class FizzBuzzBodyMovementToggleOnTest(unittest.TestCase):
    def setUp(self):
        FizzBuzz.featureToggleBodyMovement = True

    def test_given_body_movement_is_on_when_multiple_of_3_then_FizzAndTouchHead(self):
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(3))
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(51))
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(99))

    def test_given_body_movement_is_on_when_multiple_of_5_then_BuzzAndTouchShoulder(self):
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().countOff(5))
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().countOff(100))
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().countOff(50))


if __name__ == "__main__":
    unittest.main()
    
