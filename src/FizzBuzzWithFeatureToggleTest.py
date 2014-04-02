import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz

class FizzBuzzTestBodyMovementToggleOffTest(unittest.TestCase):
    def setUp(self):
        FizzBuzz.featureToggleBodyMovement = False

    def test_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))

    def test_when_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzz().countOff(3))
        self.assertEqual('Fizz', FizzBuzz().countOff(6))

    def test_when_5_then_Buzz(self):
        self.assertEqual('Buzz', FizzBuzz().countOff(5))
        self.assertEqual('Buzz', FizzBuzz().countOff(10))


class FizzBuzzBodyMovementToggleOnTest(unittest.TestCase):
    def test_when_3_then_3_with_feature_body_movement(self):
        FizzBuzz.featureToggleBodyMovement = True
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(3))
    
    def test_when_6_then_Fizz_with_feature_body_movement(self):
        FizzBuzz.featureToggleBodyMovement = True
        self.assertEqual('FizzAndTouchHead', FizzBuzz().countOff(6))

    def test_when_5_then_Buzz_with_feature_body_movement(self):
        FizzBuzz.featureToggleBodyMovement = True
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().countOff(5))

if __name__ == "__main__":
    unittest.main()
    
