import unittest

from FizzBuzzWithFeatureToggle import FizzBuzz

class FizzBuzzTestBodyMovementToggleOffTest(unittest.TestCase):
    def setUp(self):
        FizzBuzz.feature_toggle_body_movement = False

    def test_given_body_movement_is_off_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().count_off(1))
        self.assertEqual(49, FizzBuzz().count_off(49))
        self.assertEqual(98, FizzBuzz().count_off(98))

    def test_given_body_movement_is_off_when_multiple_of_3_then_Fizz(self):
        self.assertEqual('Fizz', FizzBuzz().count_off(3))
        self.assertEqual('Fizz', FizzBuzz().count_off(51))
        self.assertEqual('Fizz', FizzBuzz().count_off(99))

    def test_given_body_movement_is_off_when_multiple_of_5_then_Buzz(self):
        self.assertEqual('Buzz', FizzBuzz().count_off(5))
        self.assertEqual('Buzz', FizzBuzz().count_off(50))
        self.assertEqual('Buzz', FizzBuzz().count_off(100))

    def test_given_body_movement_is_off_when_multiple_of_3_and_5_then_FizzBuzz(self):
        self.assertEqual('FizzBuzz', FizzBuzz().count_off(15))
        self.assertEqual('FizzBuzz', FizzBuzz().count_off(45))
        self.assertEqual('FizzBuzz', FizzBuzz().count_off(90))


class FizzBuzzBodyMovementToggleOnTest(unittest.TestCase):
    def setUp(self):
        FizzBuzz.feature_toggle_body_movement = True

    def test_given_body_movement_is_on_when_common_number_then_say_it_directly(self):
        self.assertEqual(1, FizzBuzz().count_off(1))
        self.assertEqual(49, FizzBuzz().count_off(49))
        self.assertEqual(98, FizzBuzz().count_off(98))

    def test_given_body_movement_is_on_when_multiple_of_3_then_FizzAndTouchHead(self):
        self.assertEqual('FizzAndTouchHead', FizzBuzz().count_off(3))
        self.assertEqual('FizzAndTouchHead', FizzBuzz().count_off(51))
        self.assertEqual('FizzAndTouchHead', FizzBuzz().count_off(99))

    def test_given_body_movement_is_on_when_multiple_of_5_then_BuzzAndTouchShoulder(self):
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().count_off(5))
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().count_off(100))
        self.assertEqual('BuzzAndTouchShoulder', FizzBuzz().count_off(50))

    def test_given_body_movement_is_on_when_multiple_of_3_or_5_then_FizzBuzzAndTouchKnee(self):
        self.assertEqual('FizzBuzzAndTouchKnee', FizzBuzz().count_off(15))


if __name__ == "__main__":
    unittest.main()
    
