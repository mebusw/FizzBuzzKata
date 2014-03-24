import unittest


class FizzBuzzWithFeatureToggleTest(unittest.TestCase):
    def test_when_3_then_Fizz(self):
        self.assertEqual(1, FizzBuzz().countOff(1))
        self.assertEqual(2, FizzBuzz().countOff(2))
        self.assertEqual('Fizz', FizzBuzz().countOff(3))


class FizzBuzz():
    def countOff(self, n):
        if (n == 3):
            return 'Fizz'
        return n


if __name__ == "__main__":
    unittest.main()
